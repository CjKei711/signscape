from django.shortcuts import redirect, render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
def faq(request):
    return render(request, 'faq.html')
def faq_redirect(request):
    return redirect('faq')