from django.conf.urls import url, include
from stripe_cater.views import WebHookView

urlpatterns = [
    url(r'^webhooks/$', WebHookView.as_view(), name="invoice_list"),
]
