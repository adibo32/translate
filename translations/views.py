from django.shortcuts import render, redirect
from .forms import TranslationForm
from rest_framework.decorators import api_view
from .models import Employees
from django.urls import reverse


@api_view(['GET', 'POST'])
def employee_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            employee = Employees.objects.get(email=email)
        except Employees.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password.'})

        if employee.password == password:
            return redirect(reverse('translation'))

    return render(request, 'login.html')


def translation(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('translation')
    else:
        form = TranslationForm()
    return render(request, 'translation.html', {'form': form})
