from django.db import models
from django.conf import settings

class Search(models.Model):

    id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=1024)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
