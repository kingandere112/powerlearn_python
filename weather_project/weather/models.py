from django.db import models

class SearchHistory(models.Model):
    city = models.CharField(max_length=100)
    searched_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
