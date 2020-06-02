
from django.urls import path,include
from .views import index

urlpatterns = [
    path('messanger/',index,name='messanger')
]