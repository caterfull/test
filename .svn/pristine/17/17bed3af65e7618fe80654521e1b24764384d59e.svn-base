from datetime import datetime
from django.conf import settings

from django.db import models


# Create your models here.


class StripeCustomerManager(models.Manager):
    def save_local_customer(self, customer):
        local = self.create(stripeid=customer.id, stripetoken=customer.default_source)
        return local


class StripeCustomer(models.Model):
    objects = StripeCustomerManager()
    stripeid = models.CharField(max_length=50)
    stripetoken = models.CharField(max_length=50)

    def add_subscription(self, subscription):
        current_period_end = datetime.fromtimestamp(subscription.current_period_end)
        current_period_start = datetime.fromtimestamp(subscription.current_period_start)

        StripeSubscripcion.objects.create(stripecustomer=self, stripeid=subscription.id,
                                          stripestatus=subscription.status, current_period_start=current_period_start,
                                          current_period_end=current_period_end)

    def update_source(self, new_token):
        self.stripetoken = new_token

    class Meta:
        app_label = 'stripe_cater'

    def current_status(self):
        current_subs = self.subscriptions.filter(current=True).first()
        if not current_subs:
            return StripeSubscripcion.CANCELED
        return current_subs.stripestatus


class StripeSubscriptionManager(models.Manager):
    def get_by_stripe_id(self, id, ignore_current_att=False):
        query = self.filter(stripeid=id)
        if not ignore_current_att:
            query.filter(current=True)

        return query.first()


class StripeSubscripcion(models.Model):
    TRIAL = 'trialing'
    ACTIVE = 'active'
    PAST_DUE = 'past_due'
    CANCELED = 'canceled'
    UNPAID = 'unpaid'

    STATUS_CHOICES = (
        ('trialing', TRIAL),
        ('active', ACTIVE),
        ('past_due', PAST_DUE),
        ('canceled', CANCELED),
        ('unpaid', UNPAID),
    )

    objects = StripeSubscriptionManager()
    stripeid = models.CharField(max_length=50)
    stripestatus = models.CharField(max_length=50)
    stripecustomer = models.ForeignKey(StripeCustomer, related_name='subscriptions')
    current = models.BooleanField(default=True)
    current_period_start = models.DateTimeField()
    current_period_end = models.DateTimeField()

    def update_from_stripe(self, subscription_json):
        self.stripestatus = subscription_json['status']
        self.save()

    def cancel(self):
        self.current = False
        self.save()

    class Meta:
        app_label = 'stripe_cater'

    def add_invoice(self, invoice):
        created_at = datetime.fromtimestamp(invoice.date)
        StripeInvoice.objects.create(subscription=self, stripeid=invoice.id,
                                     created_at=created_at)

    def update_billing_cycle(self, start, end):
        self.current_period_start = start
        self.current_period_end = end
        self.save()

    def find_invoice(self, stripe_id):
        return self.stripeinvoice_set.filter(stripe_id=stripe_id).first()


class StripeInvoice(models.Model):
    stripeid = models.CharField(max_length=50)
    subscription = models.ForeignKey(StripeSubscripcion)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    attempt_count = models.IntegerField(default=0)
    last_attempt = models.DateTimeField(null=True)
    closed = models.BooleanField(default=False)

    def failed(self, invoice_json):
        self.attempt_count = (invoice_json['attempt_count'])
        self.last_attempt = datetime.fromtimestamp((invoice_json['date']))
        self.closed = invoice_json['closed']
        self.save()


    def success(self):
        self.paid = True
        self.closed = True
        self.save()


class EventRecord(models.Model):
    stripeid = models.CharField(max_length=50)


class PaymentOrderManager(models.Manager):
    def create_paymanet(self, amount):
        return self.create(amount=amount, due=amount)


class PaymentOrder(models.Model):
    AMOUNT_ERROR = -1

    objects = PaymentOrderManager()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    due = models.DecimalField(max_digits=9, decimal_places=2)

    def init_charge(self, amount, destination):
        if amount > self.due:
            return self.AMOUNT_ERROR

        charge = Charge(payment=self,
                        amount=amount,
                        destination=destination
        )
        return charge

    def save_charge(self, charge):
        if charge.status != Charge.PAID:
            raise RuntimeError()
        charge.save()
        self.due = self.due - charge.amount
        self.save()

    def has_been_paid(self):
        return self.due == 0


class ChargeManager(models.Manager):
    def get_charge(self, id):
        return self.filter(id=id).first()


class Charge(models.Model):
    PAID = 'PAID'
    PENDING = 'PENDING'
    FAILED = 'FAILED'

    STATUS_CHOICE = (('PAID', PAID), ('FAILED', FAILED), ('PENDING', PENDING))

    objects = ChargeManager()
    payment = models.ForeignKey(PaymentOrder)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    captured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    captured_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, default=PENDING)
    destination = models.CharField(max_length=50)
    stripe_id = models.CharField(max_length=50, null=True)
    source = models.CharField(max_length=50)
    currency = models.CharField(max_length=3, default=settings.STRIPE_DEFAULT_CURRENCY)


class StripeAccountManager(models.Manager):
    def create_account(self, stripe_publishable_key, access_token, stripe_user_id):
        return self.create(stripe_publishable_key=stripe_publishable_key, access_token=access_token,
                           stripe_user_id=stripe_user_id)


class StripeAccount(models.Model):
    objects = StripeAccountManager()
    stripe_publishable_key = models.CharField(max_length=50)
    access_token = models.CharField(max_length=50)
    stripe_user_id = models.CharField(max_length=50)
