from django.db import models

# Create your models here.

# Create your models here.


from pygments import highlight
from django.contrib.auth.models import User

class Guest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='guests', on_delete=models.CASCADE)
    highlighted = models.TextField()
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.TextField()
    class Meta:
      ordering  = ['created']

class Table(models.Model):
    created_t = models.DateTimeField(auto_now_add=True)
    owner_t = models.ForeignKey(User, related_name='tables', on_delete=models.CASCADE) #dsfcasd
    highlighted_t = models.TextField()
    name_guest = models.CharField(max_length=100, blank=True, default='')
    number_tab = models.TextField()
    tel_guest =  models.TextField()
    class Meta:
        ordering = ['created_t']
