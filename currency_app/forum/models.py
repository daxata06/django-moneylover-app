from django.db import models

class Publications(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=300)
    text = models.TextField(max_length=10000)
    author = models.TextField(max_length=50)
    likes = models.TextField(max_length=50)

class Comments(models.Model):
    id_pub = models.IntegerField()
    author = models.TextField(max_length=50)
    text = models.TextField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
