# Generated by Django 4.0.4 on 2023-04-03 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='info',
        ),
    ]
