# Generated by Django 4.2 on 2023-06-14 14:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("my_blog", "0012_alter_science_category_alter_science_image"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Science",
        ),
    ]