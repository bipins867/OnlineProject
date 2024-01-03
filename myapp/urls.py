
from . import views
from django.urls import path, include

from .views import *
urlpatterns = [
    path('register/', registerView, name='register'),
    path('login/', loginView, name='login'),
    path('dashboard/', dashboardView, name='dashboard'),
    path('profile/', profileView, name='profile'),
    path('logout/', logoutView, name='logout'),
]