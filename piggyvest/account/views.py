from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def newsletter_views(request):
    return render(request, 'newsletter.html', {'message': 'Your future self is already smiling at the progress you’re about to make.!'})

def aboutMe_views(request):
    return render(request, 'aboutMe.html', {'message': 'Things about me'})

