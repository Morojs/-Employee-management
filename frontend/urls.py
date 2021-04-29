
from django.urls import path


from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('menu',views.navbar,name='menu'),
    path('employe', views.admin, name='admin'),
]
