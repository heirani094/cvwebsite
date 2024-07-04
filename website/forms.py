# forms.py
from django import forms
from django.forms import ModelForm
#from captcha.fields import CaptchaField
from website.models import Contact

class ContactForm(ModelForm):
  #  captcha_field = CaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'
