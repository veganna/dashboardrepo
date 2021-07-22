from django.urls import path
from .views import *

app_name="core"


urlpatterns = [
    path("dashboard/", overview, name="overview"),
    path("dashboard/sales", sales, name="sales"),
    path("dashboard/expenses", expenses, name="expenses"),
    path("profile/", profile_view, name="profile"),
    path("task/", task, name="task"),
]
