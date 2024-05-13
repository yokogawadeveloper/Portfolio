from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
        



