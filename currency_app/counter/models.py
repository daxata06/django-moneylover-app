from django.db import models

class News(models.Model):
    id = models.AutoField(primary_key=True)
    pub_name = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published")
    text = models.TextField(max_length=4000)
    photo = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=100, null=True)
