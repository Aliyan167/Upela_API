from django.urls import path
from . import views

app_name = 'shipping'

urlpatterns = [
    path('', views.index, name='index'),
    path('rates/', views.rates, name='rates'),
    path('login/', views.login, name='login'),
    path('create-store/', views.create_store, name='create_store'),
    path('get-payments/', views.get_payments, name='get_payments'),
    path('select-offer/', views.select_offer, name='select_offer'),
]

