from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visualizations/', views.visualizations, name='visualizations'),
    path('predict/', views.predict, name='predict'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.doctor, name='doctor'),
    path('dodont/', views.dodont, name='dodont'),
]

urlpatterns += [
    path('upload/', views.upload_dataset, name='upload'),
]
