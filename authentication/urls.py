from django.urls import path
from authentication.views import handleLogin, handleSignup

urlpatterns = [
    path('login/', handleLogin, name="login"),
    path('signup/', handleSignup, name="signup")
]