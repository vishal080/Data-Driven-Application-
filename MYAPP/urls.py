from django.contrib import admin
from django.urls import path
from Bot import views


urlpatterns =[
    path("",views.upload_csv, name ='Bot'),
      # path("upload.html",views.upload_csv, name ='Bot'),
     
   
 path('upload/', views.upload_csv, name='upload_csv'),
    path('data/', views.data_display, name='data_display'),
    path('subscription/', views.subscription_calculator, name='subscription_calculator'),
]