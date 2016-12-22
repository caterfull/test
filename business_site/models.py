from django.conf import settings
from django.db import models
from base.models import Business
# Create your models here.


class Website(models.Model):
    template = models.IntegerField(default=1)#Ahora este campo es estatico
    business = models.ForeignKey(Business, default=0)

    def __str__(self):
        return self.business


class WebDomain(models.Model):
    domain = models.CharField(max_length=50, blank=False)
    website = models.OneToOneField(Website, default=0)

    def __str__(self):
        return self.domain


class BasicInfo(models.Model):
    logo = models.FileField(upload_to='photos', null=True)
    description = models.CharField(max_length=250, blank=False)
    website = models.OneToOneField(Website, default=0)


class Gallery(models.Model):
    comments = models.CharField(max_length=50, blank=True)
    # background = models.FileField(upload_to=settings.MEDIA_ROOT+'/photos', blank=False)
    website = models.OneToOneField(Website)


class Photo(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to='photos', blank=False)
    asbackground = models.BooleanField(default=False)
    gallery = models.ForeignKey(Gallery)


class Links(models.Model):
    twitter = models.URLField(default="twitter.com")
    instagram = models.URLField(default="instagram.com")
    facebookpage = models.URLField(default="facebook.com")
    website = models.OneToOneField(Website)


class ContactUs(models.Model):
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100, null=True)
    website = models.OneToOneField(Website)


class WebsiteControl(models.Model):
    status = models.IntegerField(default=0)#(0-create, 1-template, 2-basic, 3-gallery, 4-links, 5-contact, 6-publish)
    website = models.OneToOneField(Website)