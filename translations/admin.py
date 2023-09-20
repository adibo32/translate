from django.contrib import admin
from .models import Employees, Format, Language, Translation

admin.site.register(Employees)
admin.site.register(Format)
admin.site.register(Language)
admin.site.register(Translation)
