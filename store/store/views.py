from django.shortcuts import redirect, render

def Home(request):
    return render(request,'index.html')

def Contact(request):
    return render(request,'contact.html')

def ProductPage(request):
    return render(request, 'productpage.html')

def LoginPage(request):
    return render(request, 'login.html')

def SignupPage(request):
    return render(request, 'signup.html')