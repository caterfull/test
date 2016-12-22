__author__ = 'maykel'
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from business_site.views import WebsiteTemplate, WebsiteBasics, WebsiteGallery, WebsiteLinks, WebsiteContactUs, WebsiteCheck, WebsitePreview,\
    WebsiteCongrats, Photos, PhotosRemove, PhotosAdd
urlpatterns = patterns('',
    # Examples:
   # url(r'^$', BusinessSiteWizard.as_view([HeadInfo, BusinessInfo, ContactInfo]), name='wizard'),

    url(r'^websiteinit', WebsiteCheck.as_view(), name='websiteinit'),
    url(r'^template', login_required(WebsiteTemplate.as_view()), name='template'),
    url(r'^basic_info', login_required(WebsiteBasics.as_view()), name='basic_info'),
    url(r'^photos/$', login_required(Photos.as_view()), name='photos'),
    url(r'^photos/add$', login_required(PhotosAdd.as_view()), name='photos_add'),
    url(r'^photos/remove/(?P<id>\d+)$', login_required(PhotosRemove.as_view()), name='photos_remove'),

    url(r'^gallery', login_required(WebsiteGallery.as_view()), name='gallery'),
    url(r'^links', login_required(WebsiteLinks.as_view()), name='links'),
    url(r'^contactus',login_required(WebsiteContactUs.as_view()), name='contactus'),
    url(r'^preview', login_required(WebsitePreview.as_view()), name='preview'),
    url(r'^congrats',login_required(WebsiteCongrats.as_view()), name='congrats'),

)