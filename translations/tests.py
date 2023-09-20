from django.test import TestCase
from .models import Employees, Format, Language, Translation
from django.urls import reverse
from rest_framework.test import APIClient


class TranslationTestCase(TestCase):

    def setUp(self):
        self.format = Format.objects.create(name="Test Format", format_type="ios")
        self.language = Language.objects.create(name="English", code="en")
        self.translation = Translation.objects.create(
            format=self.format, text="Hallo", language=self.language, translation="Hello")

    def test_create_employee(self):
        employee = Employees.objects.create(email="test@test.com", password="password")
        self.assertEqual(employee.email, "test@test.com")

    def test_create_format(self):
        format = Format.objects.create(name="Test Format", format_type="android")
        self.assertEqual(format.name, "Test Format")

    def test_create_language(self):
        language = Language.objects.create(name="English", code="en_US")
        self.assertEqual(language.code, "en_US")

    def test_create_translation(self):
        translation = Translation.objects.create(
            format=self.format, text="Hallo", language=self.language, translation="Hello")
        self.assertEqual(translation.text, "Hallo")


class EmployeeLoginTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.login_url_invalid = reverse('login')
        self.login_url_valid = reverse('translation')
        self.valid_payload = {
            'email': 'employee@example.com',
            'password': 'password123'
        }
        self.invalid_payload = {
            'email': 'invalid@example.com',
            'password': 'password123'
        }

    def test_valid_login(self):
        response = self.client.post(
            self.login_url_valid,
            self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = self.client.post(
            self.login_url_invalid,
            self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, 200)


class TranslationViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.format = Format.objects.create(name="Test Format", format_type="ios")
        self.language = Language.objects.create(name="Test Language", code="en")
        self.url = reverse('translation')

    def test_translation_view_post_valid_data(self):
        data = {
            'format': self.format.pk,
            'text': 'Hallo',
            'language': self.language.pk,
            'translation': 'Hello'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Translation.objects.filter(translation='Hello').exists())

    def test_translation_view_post_invalid_data(self):
        data = {
            'format': self.format.pk,
            'text': '',
            'language': self.language.pk,
            'translation': 'Hello'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Translation.objects.filter(translation='Hello').exists())
