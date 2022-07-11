from django.urls import path

from login import views as vlogin
urlpatterns = [
   path('', vlogin.Login, name='login'),
  
]