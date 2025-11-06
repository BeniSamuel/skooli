from django.shortcuts import render

# Create your views here.
def handleLogin (request):
    if request.method == "POST":
        pass
    else:
        return render(request, "login/login.html")

def handleSignup (request):
    if request.method == "POST":
        pass
    else:
        return render(request, "signup/signup.html")
