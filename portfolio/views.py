from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('My portfolio in Moringa Core')

def projects(request):
  return render(request, 'home.html')