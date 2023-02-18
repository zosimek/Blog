from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_one(request):
    return render(request, 'try_one.html')
