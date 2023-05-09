from django.forms import ModelForm
from website.models import *
from captcha.fields import CaptchaField

class ContactForm(ModelForm):
    captcha = CaptchaField()
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].required = False
        
    class Meta:
        model = Contact
        fields = '__all__'
        

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
    
        