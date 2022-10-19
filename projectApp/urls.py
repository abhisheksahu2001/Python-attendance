
from django.urls import path
#now import the views.py file into this code
from . import views


urlpatterns= [
  path('', views.home, name='home'),
  path('save/', views.save_attend, name='save'),
]