from django.forms import ModelForm
from blog.models import *
from captcha.fields import CaptchaField

class CommentForm(ModelForm):
    captcha = CaptchaField()
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['subject'].required = False
        
    class Meta:
        model = Comment
        fields = ['post','name','email','subject','message']
