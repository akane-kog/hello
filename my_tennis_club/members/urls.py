from django.urls import path
from . import views
from. import test_views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='mambers'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
