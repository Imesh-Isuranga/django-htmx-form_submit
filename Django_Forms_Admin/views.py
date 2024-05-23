from django.shortcuts import render

from .forms import ContactForm


# Create your views here.
def index(request):
    context = {'form': ContactForm()}
    return render(request,'index.html',context)
