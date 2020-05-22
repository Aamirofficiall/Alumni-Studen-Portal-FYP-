from django.shortcuts import render

def index(request):
    return render(request,'frontend/dist/index.html')