from rest_framework import viewsets
from .serializers import EmployeesSerializer, FormatSerializer, LanguageSerializer, TranslationSerializer
from .models import Employees, Format, Language, Translation


class EmployeesAPI (viewsets.ReadOnlyModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class FormatAPI (viewsets.ReadOnlyModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


class LanguageAPI (viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class TranslationAPI (viewsets.ReadOnlyModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
