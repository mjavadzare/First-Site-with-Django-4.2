from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True, blank=True, default=None)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return "{} - {}".format(self.name, self.subject)
    
class Newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email