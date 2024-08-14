from django.db import models

# Create your models here.

class PageVisit(models.Model):
    # db - > Table
    # invis col id -> primary key -> autofield -> 1,2,3, etc
    path = models.TextField(null=True, blank=True) 
    timestamp = models.DateTimeField(auto_now_add=True)
    ...