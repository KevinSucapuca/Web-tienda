from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('SearchProducto/', views.SearchProducto, name='SearchProducto'),
    path('Liquidacion/', views.Liquidacion, name='Liquidacion'),
    path('SearchLiquidacion/', views.SearchLiquidacion, name='SearchLiquidacion'),
    path('productos/tag/<str:tag_slug>/', views.mostrar_productos_por_tag, name='productos_por_tag'),
    path('detalle_producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),

]