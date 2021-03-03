from django.shortcuts import render

# Create your views here.


#Index Page 
def index(request):
    return render(request, 'pages/index.html')


#About Us Page View
def about(request):
    return render(request, 'pages/about.html')

#Services View Page
def services(request):
    return render(request, 'pages/services.html')



#Contact Us View
def contactus(request):
    return render (request, 'pages/contactus.html')


#Profolio View
def products(request):
    return render(request, 'pages/products.html')

    