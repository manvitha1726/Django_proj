from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('home.html',views.home,name='home'),
    path('myths.html',views.myths,name='myths'),
    path('pros.html',views.pros,name='pros'),
    path('cons.html',views.cons,name='cons'),
    path('contact.html',views.contact,name='contact'),

    
]
