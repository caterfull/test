from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from django.views.generic.base import View
from base.forms import CustomerForm, EventForm
from base.models import Business, Customer
from django.contrib import messages
from base.util import check_permission


class CustomerView(View):

    def get(self, request, *args, **kwargs):



        user = request.user
        id = kwargs.get('id')
        business = Business.objects.filter(owner=user).first()
        if id:
                # customer = Customer.objects.filter(id=id).filter(business=business).first()
                customer = Customer.objects.get_one_by_business_and_id(business, id)
                if customer:
                    return render_to_response("base/customer/customer.html", RequestContext(request,{'customer':customer}))
                else:
                    return HttpResponse(status=404)

        else:

            # messages.success(request, 'Se ha creado satisfactoriamnte el cliente especificado')
            # messages.error(request, 'Se ha creado satisfactoriamnte el cliente especificado')
            # messages.info(request, 'Se ha creado satisfactoriamnte el cliente especificado')
            # messages.warning(request, 'Se ha creado satisfactoriamnte el cliente especificado')
            #
            customers = Customer.objects.list_by_business(business)
            if request.is_ajax():
                return render_to_response("base/customer/table.html",RequestContext(request, {'customers':customers}))


            return render_to_response("base/customer/customers.html", RequestContext(request, {'customers':customers, 'model':"Clientes", 'description':"Listado de clientes"}))

class CustomeRegisterView(View):

    def get(self, request, *args, **kwargs):
        if not check_permission(request=request, permission='add_customer'):
           return HttpResponseRedirect(redirect_to=reverse('login'))
        form = CustomerForm()
        return render_to_response("base/customer/form.html", RequestContext(request, {'form':form}))

    def post(self, request, *args, **kwargs):
        if not check_permission(request=request, permission='add_customer'):
           return HttpResponseRedirect(redirect_to=reverse('login'))
        form = CustomerForm(request.POST)
        errors = {}
        if form.is_valid():
            user = request.user
            business = Business.objects.filter(owner=user).first()
            response = Customer.objects.create_or_update_customer(form.cleaned_data, business)
            if response in Customer.objects.ERRORS:

                if response == Customer.objects.EMAIL_ERROR:
                    errors['unique_email'] = "Correo Repetido"

                return render_to_response("base/customer/form.html", RequestContext(request, {'form':form, 'errors':errors}),status=400)

            # messages.success(request, 'Se ha creado satisfactoriamnte el cliente especificado')
            return JsonResponse(data={'id':response.id},status=200)
        else:
            print("error")
            return render_to_response("base/customer/form.html", RequestContext(request, {'form':form,'errors':errors}),status=400)

class CustomerRemoveView(View):

    def post(self, request, *args, **kwargs):
        if not check_permission(request=request, permission='remove_customer'):
           return HttpResponseRedirect(redirect_to=reverse('login'))
        id = kwargs.get('id')
        user = request.user
        business = Business.objects.filter(owner=user).first()

        Customer.objects.delete_by_business(id=id, business=business)
        # messages.success(request, 'Se ha eliminado satisfactoriamnte el cliente ')
        return HttpResponse(status=200)
        # return HttpResponseRedirect(redirect_to=reverse('customers'))

class CustomerEditView(View):

    def set_data_from_customer(self, customer):
        company = None
        if customer.company:
            company = customer.company.text
        return {'first_name':customer.first_name, 'last_name':customer.last_name,
                'email':customer.email, 'comments':customer.comments, 'company':company}

    def get(self, request, *args, **kwargs):
        if not check_permission(request=request, permission='edit_customer'):
           return HttpResponseRedirect(redirect_to=reverse('login'))
        id = kwargs.get('id')
        user = request.user
        business = Business.objects.filter(owner=user).first()

        customer = Customer.objects.get_one_by_business_and_id(business=business, id=id)

        if customer:
            form = CustomerForm(instance=customer, initial=self.set_data_from_customer(customer))
            return render_to_response("base/customer/form.html", RequestContext(request,{'form':form}))
        else:
            return HttpResponse(status=404)

    def post(self, request, *args, **kwargs):
        if not check_permission(request=request, permission='edit_customer'):
           return HttpResponseRedirect(redirect_to=reverse('login'))
        id = kwargs.get('id')

        user = request.user
        business = Business.objects.filter(owner=user).first()

        customer = Customer.objects.get_one_by_business_and_id(business=business, id=id)

        if customer:
            form = CustomerForm(request.POST)
            errors = {}
            if form.is_valid():
                response = Customer.objects.create_or_update_customer(form.cleaned_data,business, customer)
                if response in Customer.objects.ERRORS:
                    if response == Customer.objects.EMAIL_ERROR:
                        errors['unique_email'] = "Correo Repetido"
                    return render_to_response("base/customer/form.html", RequestContext(request,{'form':form,'errors':errors}))

                #messages.success(request, 'Se ha creado satisfactoriamnte el cliente especificado')
                return HttpResponseRedirect(redirect_to=reverse('customers'))
            else:
                return render_to_response("base/customer/form.html", RequestContext(request,{'form':form,'errors':errors}))
        else:
            return HttpResponse(status=404)

class CustomerSelectView(View):

    def get(self, request, *args, **kwargs):
        user = request.user

        id = request.GET.get('id')
        if id:

            customer = Customer.objects.get(pk=id)
        else:
            customer = None
        business = Business.objects.filter(owner=user).first()
        # customers = Customer.objects.list_by_business(business)

        form = EventForm(initial={'customer':customer.id,'business':business})
        return render_to_response('base/customer/select.html', RequestContext(request, {'form':form}))