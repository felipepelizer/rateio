from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rateio_site import views

router = routers.DefaultRouter()
router.register(r'rateio_site', views.Cost_Center_View, 'rateio_site')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('rateio_site.urls')),
]
