# Generated by Django 5.0.3 on 2024-06-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_alter_publication_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='photo_pub_path',
        ),
        migrations.AddField(
            model_name='publication',
            name='photo',
            field=models.ImageField(null=True, upload_to='currency_app/counter/static'),
        ),
    ]
