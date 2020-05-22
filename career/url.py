from django.urls import path,include
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    path('',CareerDisplay,name='careerDisplay'),
    path('<int:id>/',CareerDisplayDetail,name='careerDisplayDetail'),
    path('add/',AddCareer,name='addCareer'),
    path('update/<int:id>/',UpdateCareer,name='updateCareer'),
    path('delete/<int:id>/',DeleteCareer,name='deleteCareer'),
]
