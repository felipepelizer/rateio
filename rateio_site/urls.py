from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('register', views.register_user, name="register"),

    path('cost_center', views.cost_center, name="cost_center"),
    path('cost_center_create', views.cost_center_create, name="cost_center_create"),
    path('cost_center_edit/<int:id>', views.cost_center_edit, name="cost_center_edit"),
    path('cost_center_delete/<int:id>', views.cost_center_delete, name="cost_center_delete"),

    path('product', views.product, name="product"),
    path('product_create', views.product_create, name="product_create"),
    path('product_edit/<int:id>', views.product_edit, name="product_edit"),
    path('product_delete/<int:id>', views.product_delete, name="product_delete"),

    path('employee', views.employee, name="employee"),
    path('employee_create', views.employee_create, name="employee_create"),
    path('employee_edit/<int:id>', views.employee_edit, name="employee_edit"),
    path('employee_delete/<int:id>', views.employee_delete, name="employee_delete"),

    path('squad', views.squad, name="squad"),
    path('squad_create', views.squad_create, name="squad_create"),
    path('squad_edit/<int:id>', views.squad_edit, name="squad_edit"),
    path('squad_delete/<int:id>', views.squad_delete, name="squad_delete"),


]
