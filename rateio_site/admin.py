from django.contrib import admin
from .models import Department, Business, Company, Allocation_Type, Status_Cost_Center, Cost_Center
from .models import Status_Product, Segment, Product
from .models import Access_Type, Position, City, Contract_Type, Vendor, Status_Employee, Employee
from .models import Squad_Group, Status_Squad, Squad
from .models import Month, Status_Scenario, Scenario

admin.site.register(Department)
admin.site.register(Business)
admin.site.register(Company)
admin.site.register(Allocation_Type)
admin.site.register(Status_Cost_Center)
admin.site.register(Cost_Center)

admin.site.register(Status_Product)
admin.site.register(Segment)
admin.site.register(Product)

admin.site.register(Access_Type)
admin.site.register(Position)
admin.site.register(City)
admin.site.register(Contract_Type)
admin.site.register(Vendor)
admin.site.register(Status_Employee)
admin.site.register(Employee)

admin.site.register(Squad_Group)
admin.site.register(Status_Squad)
admin.site.register(Squad)

admin.site.register(Month)
admin.site.register(Status_Scenario)
admin.site.register(Scenario)
