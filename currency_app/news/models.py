from django.db import models
from counter.models import *

class Comments_news(models.Model):
    news_id = models.IntegerField()
    author = models.TextField(max_length=50)
    text = models.TextField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
