# blog/views.py
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def home_view(request):
    return render(request, 'home.html', {'message': 'welcome to my Django homepage!'})

def form_view(request):
    return render(request, 'form.html', {'message': 'Feel free your Data is safe with me!'})