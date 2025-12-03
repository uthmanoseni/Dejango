from django.shortcuts import render

# Create your views here.

# views.py
from django.shortcuts import render, redirect
from .forms import MyContactForm

def contact_view(request):
    if request.method == 'POST':
        form = MyContactForm(request.POST)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # ... perform actions like sending an email or saving to DB
            return redirect('success_page') # Redirect to a success page
    else:
        form = MyContactForm() # Create an empty form for GET request
    return render(request, 'contact.html', {'form': form})

