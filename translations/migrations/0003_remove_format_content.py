# Generated by Django 3.1.6 on 2023-03-21 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0002_auto_20230321_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='format',
            name='content',
        ),
    ]