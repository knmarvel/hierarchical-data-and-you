from django.shortcuts import render
from filecabinet.models import File

# Create your views here.
def index(request):
    html = 'index.html'
    data = File.objects.all()
    
    return render(request, html, {'data': data})
