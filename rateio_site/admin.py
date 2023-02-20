from django.contrib import admin
from .models import Department, Business, Company, Allocation_Type, Status_Cost_Center, Cost_Center
from .models import Status_Product, Segment, Product

admin.site.register(Department)
admin.site.register(Business)
admin.site.register(Company)
admin.site.register(Allocation_Type)
admin.site.register(Status_Cost_Center)
admin.site.register(Cost_Center)

admin.site.register(Status_Product)
admin.site.register(Segment)
admin.site.register(Product)