from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('SearchProducto/', views.SearchProducto, name='SearchProducto'),
    path('detalle_producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),

]