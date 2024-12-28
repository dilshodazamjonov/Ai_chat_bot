from django.urls import path
from .views import *

urlpatterns = [
    path('', chatbot_views, name='chatbot')
]