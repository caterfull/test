from urllib.parse import urlencode
import datetime

from django.conf import settings
from django.contrib.sites import requests
from django.core.urlresolvers import reverse
from django.db import transaction
from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.base import View
from base.model_invoice import Invoice

from base.models import Business
from base.util import check_permission
from caterfull.settings import STRIPE_CLIENTE_ID, STRIPE_API_KEY
from stripe_cater.services import ERRORS, create_charge_on_paymentorder, update_customer_source
from stripe_cater.services import create_account, initial_subscribe_bussines

# basic
class StripeSubscribeView(View):

    def get(self, request, *args, **kwargs):
        if not check_permission(request=request, permission='update_subscription'):
           return HttpResponseRedirect(redirect_to=reverse('login'))
        business_id = kwargs.get('business_id')
        PUBLISHABLE_KEY = settings.STRIPE_PUBLISHABLE_KEY
        return render_to_response('base/stripe_account/subscribe.html', RequestContext(request, {'PUBLISHABLE_KEY':PUBLISHABLE_KEY,'business_id':business_id}))

    def post(self, request, *args, **kwargs):
        if not check_permission(request=request, permission='update_subscription'):
           return HttpResponseRedirect(redirect_to=reverse('login'))
        PUBLISHABLE_KEY = settings.STRIPE_PUBLISHABLE_KEY
        business_id = kwargs.get('business_id')
        business = Business.objects.get_business_by_id(id=business_id)
        stripeToken = request.POST.get('stripeToken')
        response = None
        try:
            with transaction.atomic():
                response = update_customer_source(newtoken=stripeToken, localcustomer=business.stripecustomer)
                if response in ERRORS:
                    raise RuntimeError()
                business.set_stripe_customer(customer=response)

                return render_to_response('base/stripe_account/subscribe.html', RequestContext(request, {
                    'error':response,
                    'succeed':True,
                    'PUBLISHABLE_KEY':PUBLISHABLE_KEY,'business_id':business_id}))
        except:
            return render_to_response('base/stripe_account/subscribe.html', RequestContext(request, {'error':response,'PUBLISHABLE_KEY':PUBLISHABLE_KEY,'business_id':business_id}))

            # return JsonResponse(status=400, data={'error':response})

# trial
class StripeAuthorizeView(View):

    def get(self, request, *args, **kwargs):
        business_id = kwargs.get('business_id')
        return render_to_response('base/stripe_account/connect_stripe.html', RequestContext(request, {'business_id':business_id}))

    def post(self, request, *args, **kwargs):
        business_id = kwargs.get('business_id')
        business = Business.objects.get_business_by_id(id=business_id)
        if not business or business.has_an_account():
            return HttpResponse(status=404)
        else:
            state = business.regenerate_token()
            site = settings.STRIPE_OAUTH_SITE + settings.STRIPE_AUTHORIZE_URI
            params = {
                "response_type": "code",
                "scope": "read_write",
                "client_id": settings.STRIPE_CLIENTE_ID,
                'state':state,
                'redirect_uri':settings.CATERFULL_BASE_URL + reverse('stripe_callback')
              }

            # Redirect to Stripe /oauth/authorize endpoint
            url = site + '?' + urlencode(params)
            return redirect(url)

class StripeCallbackView(View):

    def get(self, request, *args, **kwargs):

        code = request.args.get('code')
        state = request.args.get('state')

        business = Business.objects.get_by_token(token=state)
        if not business:
            return HttpResponse(status=404)

        data = {
            "grant_type": "authorization_code",
            "client_id": STRIPE_CLIENTE_ID,
            "client_secret": STRIPE_API_KEY,
            "code": code
        }

        # Make /oauth/token endpoint POST request
        url = settings.STRIPE_OAUTH_SITE + settings.STRIPE_TOKEN_URI
        resp = requests.post(url, params=data)

        access_token = resp.json().get('access_token')
        stripe_user_id = resp.json().get('stripe_user_id')
        stripe_publishable_key = resp.json().get('stripe_publishable_key')

        try:
            with transaction.atomic():
                account = create_account(access_token=access_token, stripe_user_id=stripe_user_id,
                                         stripe_publishable_key=stripe_publishable_key)

                business.set_account(account=account)

        except:
             return HttpResponse(status=500)
        if request.user.is_authenticated():
             return HttpResponseRedirect(redirect_to=reverse('dashboard'))
        return render_to_response('base/stripe_account/account_succeed.html', RequestContext(request,{'account':account,
                                                                                                      'business':business}))
class InvoiceCharge(View):

    def get(self, request, *args, **kwargs):
        idempotency = int(datetime.datetime.today().timestamp())
        invoice_id = kwargs.get('iidb64')
        # print(invoice_id)
        invoice_id = force_text(urlsafe_base64_decode(invoice_id))
        token = kwargs.get('token')
        token = force_text(urlsafe_base64_decode(token))
        # print(invoice_id, token)
        invoice = Invoice.objects.get_invoice_to_pay_by_id(id=invoice_id, token=token)
        if not invoice:
            return HttpResponse(status=404)

        account = invoice.proposal.event.customer.business.stripe_account
        payment_order = invoice.payment_order
        return render_to_response('base/stripe_account/invoice_charge.html', RequestContext(request,{
            'invoice':invoice, 'account':account, 'idempotency':idempotency,'payment_order':payment_order}))

    def post(self, request, *args, **kwargs):
        idempotency = request.POST.get('idempotency')

        invoice_id = kwargs.get('iidb64')
        invoice_id = force_text(urlsafe_base64_decode(invoice_id))
        token = kwargs.get('token')
        token = force_text(urlsafe_base64_decode(token))
        invoice = Invoice.objects.get_invoice_to_pay_by_id(id=invoice_id, token=token)
        if not invoice:
            return HttpResponse(status=404)
        stripeToken = request.POST.get('stripeToken')
        amount = request.POST.get('amount')

        payment_order = invoice.payment_order
        account = invoice.proposal.event.customer.business.stripe_account
        response = create_charge_on_paymentorder(idempotency_key=idempotency,amount=amount, source=stripeToken, stripe_account=account.stripe_user_id, paymentorder=payment_order)

        if response in ERRORS:
             return render_to_response('base/stripe_account/invoice_charge.html', RequestContext(request,{
            'invoice':invoice, 'account':account, 'idempotency':idempotency,'payment_order':payment_order,
             'errors':response}),
                                       status=400)

        invoice.check_status()
        return render_to_response('base/stripe_account/invoice_charge.html', RequestContext(request,{
            'invoice':invoice, 'account':account, 'idempotency':idempotency,'payment_order':payment_order}))
