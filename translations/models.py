from django.db import models

# Create your models here.


class Employees(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=100, default='')
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.email


class Format(models.Model):
    id = models.BigAutoField(primary_key=True)
    FORMAT_CHOICES = (
        ('ios', 'iOS (.strings)'),
        ('android', 'Android (.xml)'),
    )
    name = models.CharField(max_length=100)
    format_type = models.CharField(max_length=10, choices=FORMAT_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_format_type_display()})"


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.code


class Translation(models.Model):
    id = models.BigAutoField(primary_key=True)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='destination_translations')
    translation = models.TextField()

    def __str__(self):
        return self.translation + " on " + self.format.name
