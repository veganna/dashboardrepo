from django.urls import path
from .views import *

app_name='accounts'

urlpatterns = [
    path('login/', loginPage, name="login"),
    path('logout/', logoutPage, name="logout"),
]