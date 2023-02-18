# Generated by Django 4.1.7 on 2023-02-16 02:52

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertise', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=64)),
                ('middleName', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('lastName', models.CharField(default='', max_length=64)),
                ('info', ckeditor.fields.RichTextField(blank=True, default="... haven't decided yet ...", null=True)),
                ('readyToLounch', models.BooleanField(default=False)),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_blog.expertise')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=124, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('tags', models.CharField(default='', max_length=200, unique=True)),
                ('mainBody', ckeditor.fields.RichTextField(blank=True, default='... to be continued ...', null=True)),
                ('readyToLounch', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_blog.user')),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_blog.expertise')),
            ],
        ),
    ]