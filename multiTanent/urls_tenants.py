from django.urls import path
from customers.views import tenant
urlpatterns = [
    path('', tenant),
]