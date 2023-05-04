from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField 
from django.core.exceptions import ValidationError
from  datetime import date

# Create your models here.

class Project(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max image size is %sMB" % str(megabyte_limit))
    image = models.ImageField(upload_to='projects/', default='projects/default.png', validators=[validate_image])
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField( max_length=120 , default='website', null=False)
    title = models.CharField(max_length=250, default='website', null=False )
    content = RichTextUploadingField() # CKEditor Rich Text Field
    StartTime = models.DateField(null = False, default=date.today)
    FinishedTime = models.DateField(null = False, default=date.today)
    customer = models.CharField(max_length=120 , default='unknown')

    publish_status = models.BooleanField(default=False, )
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return "{} - {}".format(self.title, self.id)
    
    def get_absolute_url(self):
        return reverse('projects:single', kwargs={'pid':self.id})
    