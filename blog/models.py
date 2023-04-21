from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField 
from django.core.exceptions import ValidationError
from blog.formatChecker import ContentTypeRestrictedFileField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Post(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max image size is %sMB" % str(megabyte_limit))
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg', validators=[validate_image])
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    content = RichTextUploadingField() # CKEditor Rich Text Field
    audio = ContentTypeRestrictedFileField(upload_to='uploads/',
                                              content_types=[ 'audio/mpeg' ],
                                              max_upload_size=20971520,blank=True, null=True, verbose_name='audio') #'video/x-msvideo', 'application/pdf', 'video/mp4',
    video = ContentTypeRestrictedFileField(upload_to='uploads/',
                                              content_types=['video/mp4'],
                                              max_upload_size=20971520,blank=True, null=True, verbose_name='video')
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    counted_views = models.PositiveIntegerField(default=0)
    publish_status = models.BooleanField(default=False, )
    published_date = models.DateTimeField(null=True)
    login_require = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return "{} - {}".format(self.title, self.id)
    
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    email = models.EmailField()
    subject = models.CharField(max_length=200, null=True, blank=True, default=None)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_date',)
    def __str__(self):
        return self.name
    