# Generated by Django 4.1.7 on 2023-04-18 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0004_tag_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='author',
        ),
    ]
