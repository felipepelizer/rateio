from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    
    path('cost_center', views.cost_center, name="cost_center"),
    path('cost_center_create', views.cost_center_create, name="cost_center_create"),
    path('cost_center_edit/<int:id>', views.cost_center_edit, name="cost_center_edit"),
    path('cost_center_delete/<int:id>', views.cost_center_delete, name="cost_center_delete"),

    path('product', views.product, name="product"),
    path('product_create', views.product_create, name="product_create"),
    path('product_edit/<int:id>', views.product_edit, name="product_edit"),
    path('product_delete/<int:id>', views.product_delete, name="product_delete"),
]
