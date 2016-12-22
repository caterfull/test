__author__ = 'maykel'

from django import forms


class TemplateChoice(forms.Form):
    template = forms.ChoiceField(required=True, initial=1, choices=((1, 'Template 1'), ), widget=forms.RadioSelect())


class BasicInfoForm(forms.Form):
    # form1 wizard
    # company_name = forms.CharField(widget=forms.TextInput, max_length=100)
    logo = forms.FileField(widget=forms.FileInput, required=False)
    description = forms.CharField(widget=forms.Textarea, max_length=250, required=True)


class GalleryForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, max_length=100, required=True)
    image = forms.FileField(widget=forms.FileInput, required=True)


class LinksForm(forms.Form):
    twitter = forms.URLField(widget=forms.TextInput, max_length=30)
    instagram = forms.URLField(widget=forms.TextInput, max_length=30)
    facebook_page = forms.URLField(widget=forms.TextInput, max_length=30)


class ContactUsForm(forms.Form):
    fields = {'country_code': forms.CharField(), 'phone_number': forms.IntegerField(),
              'extension': forms.IntegerField()}
    # phone = forms.PhoneField(fields=fields, widget=forms.MultiValueField, required=False)
    phone = forms.CharField(widget=forms.TextInput, required=False)
    email = forms.EmailField(widget=forms.EmailInput, required=False)
    address = forms.CharField(widget=forms.TextInput, max_length=100, required=False)
    from django.core.validators import RegexValidator

    # class PhoneField(MultiValueField):
    #     def __init__(self, *args, **kwargs):
    #         # Define one message for all fields.
    #         error_messages = {'incomplete': 'Enter a country calling code and a phone number.', }
    #         # Or define a different message for each field.
    #         fields = (CharField(
    #             error_messages={'incomplete': 'Enter a country calling code.'},
    #             validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid country calling code.'), ],
    #         ),
    #                   CharField(error_messages={'incomplete': 'Enter a phone number.'},
    #                             validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')],
    #                   ),
    #                   CharField(validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid extension.')], required=False, ),
    #         )
    #         super(PhoneField, self).__init__(error_messages=error_messages, fields=fields, require_all_fields=False,
    #                                          *args, **kwargs)
    #

    #
    # class HeadInfo(forms.Form):d
    # #form1 wizard
    #     title = forms.CharField(widget=forms.TextInput, max_length=100)
    #     slogan = forms.CharField(widget=forms.TextInput, max_length=100)
    #     logo = forms.ImageField(widget=forms.FileInput, required=False)
    #
    # class BusinessInfo(forms.Form):
    #     #form2 wizard
    #     description = forms.CharField(widget=forms.Textarea)
    #     image = forms.ImageField(widget=forms.FileInput, required=False)
    #
    # class ContactInfo(forms.Form):
    #     #form3 wizard
    #     phone_number = forms.IntegerField(widget=forms.NumberInput)
    #     email = forms.EmailField(widget=forms.EmailInput)
    #     address = forms.CharField(widget=forms.TextInput)
    #     web = forms.CharField(widget=forms.TextInput)