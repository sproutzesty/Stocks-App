from django.urls import path
from stocks import views

urlpatterns = [
    path('stocks/', views.stock_list),
    path('stocks/<int:pk>/', views.stock_detail),
]