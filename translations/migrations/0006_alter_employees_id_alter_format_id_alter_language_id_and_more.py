# Generated by Django 4.1.3 on 2023-03-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0005_rename_translator_translation_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='format',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='translation',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
