from django.shortcuts import render

# Create your views here.


#Index Page 
def index(request):
    return render(request, 'pages/index.html')


#Index Page 
def about(request):
    return render(request, 'pages/about.html')


