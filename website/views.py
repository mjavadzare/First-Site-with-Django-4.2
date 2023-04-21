from django.shortcuts import render, HttpResponseRedirect
from website.forms import *
from django.contrib import messages
# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.name = 'Unknown'     # warning simple-captcha is enabled.
            new_contact.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submited successfully.')
        else:
            messages.add_message(request, messages.ERROR, "Your ticket didn't submit, make sure you have a valid ticket and try again.")
    form = ContactForm()
    return render(request, 'website/contact.html' , context={'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your email submited successfully.')
        else:
            messages.add_message(request, messages.ERROR, "Your email sent didn't submit, make sure you write a valid email and try again.")
    form = NewsletterForm()
    return render(request, 'website/index.html' , context={'form': form})

# from django.shortcuts import redirect

# def redirect_view(request):
# #     response = redirect('/redirect-success/')
#     return render(request, 'mending.html')