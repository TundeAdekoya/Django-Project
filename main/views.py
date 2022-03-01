from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse("""<h1>This is a simple view</h1>
                        <br>
                        <h2>Testing this GUY</h2>
    
    
    """)
