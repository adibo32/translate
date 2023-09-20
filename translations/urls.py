from django.urls import path, include
from .api import EmployeesAPI, FormatAPI, LanguageAPI, TranslationAPI
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'employees', EmployeesAPI, basename='user')
router.register(r'format', FormatAPI)
router.register(r'language', LanguageAPI)
router.register(r'translation', TranslationAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.employee_login, name='login'),
    path('home/', views.translation, name='translation'),
]
