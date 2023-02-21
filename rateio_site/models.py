from django.db import models
from django.contrib.auth.models import User


##############################
##### Cost Center Models #####
##############################

class Department (models.Model):
	pk_department = models.IntegerField(primary_key=True, verbose_name = "ID Department")
	desc_department = models.CharField(max_length=512, verbose_name = "Department")
	desc_pl_group = models.CharField(max_length=512, default = None, verbose_name = "P&L Group")

	class Meta:
		verbose_name_plural = "Department"

	def __str__(self):
		return self.desc_department


class Business (models.Model):
	pk_business = models.IntegerField(primary_key=True, verbose_name = "ID Business")
	desc_business = models.CharField(max_length=512, verbose_name = "Business")

	class Meta:
		verbose_name_plural = "Business"

	def __str__(self):
		return self.desc_business


class Company (models.Model):
	pk_company = models.IntegerField(primary_key=True, verbose_name = "ID Company")
	desc_company = models.CharField(max_length=512, verbose_name = "Company")

	class Meta:
		verbose_name_plural = "Company"

	def __str__(self):
		return self.desc_company	


class Allocation_Type (models.Model):
	pk_allocation_type = models.IntegerField(primary_key=True,  verbose_name = "ID Allocation Type")
	code_allocation_type = models.CharField(max_length=513, verbose_name = "Allocation Type Code")
	desc_allocation_type = models.CharField(max_length=512, default = None, verbose_name = "Allocation Type")

	class Meta:
		verbose_name_plural = "Allocation Type"

	def __str__(self):
		return self.desc_allocation_type


class Status_Cost_Center (models.Model):
	pk_status_cost_center = models.IntegerField(primary_key=True, verbose_name = "ID Status Cost Center")
	desc_status_cost_center = models.CharField(max_length=512, verbose_name = "Status Cost Center")

	class Meta:
		verbose_name_plural = "Status Cost Center"

	def __str__(self):
		return self.desc_status_cost_center


class Cost_Center (models.Model):
	pk_cost_center = models.IntegerField(primary_key=True, verbose_name = "ID Cost Center")
	code_cost_center = models.CharField(max_length=512, verbose_name = "Cost Center Code")
	desc_cost_center = models.CharField(max_length=512, verbose_name = "Cost Center")
	fk_department = models.ForeignKey (Department, default = 1, verbose_name = "Department", on_delete = models.SET_DEFAULT)
	fk_business = models.ForeignKey (Business, default = 1, verbose_name = "Business", on_delete = models.SET_DEFAULT)
	fk_company = models.ForeignKey (Company, default = 1, verbose_name = "Company", on_delete = models.SET_DEFAULT)
	fk_allocation_type = models.ForeignKey (Allocation_Type, default = 1, verbose_name = "Allocation Type", on_delete = models.SET_DEFAULT)
	fk_status_cost_center = models.ForeignKey (Status_Cost_Center, default = 1, verbose_name = "Status Cost Center", on_delete = models.SET_DEFAULT)

	class Meta:
		verbose_name_plural = "Cost Center"

	def __str__(self):
		return self.desc_cost_center


##############################
####### Product Models #######
##############################

class Status_Product (models.Model):
	pk_status_product = models.IntegerField(primary_key=True, verbose_name = "ID Status Product")
	desc_status_product = models.CharField(max_length=512, verbose_name = "Status Product")

	class Meta:
		verbose_name_plural = "Status Product"

	def __str__(self):
		return self.desc_status_product


class Segment (models.Model):
	pk_segment = models.IntegerField(primary_key=True, verbose_name = "ID Segment")
	desc_segment = models.CharField(max_length=512, verbose_name = "Segment")

	class Meta:
		verbose_name_plural = "Segment"

	def __str__(self):
		return self.desc_segment


class Product (models.Model):
	pk_product = models.IntegerField(primary_key=True, verbose_name = "ID Product")
	desc_product = models.CharField(max_length=512, verbose_name = "Product")
	fk_segment = models.ForeignKey (Segment, default = 1, verbose_name = "Segment", on_delete = models.SET_DEFAULT)
	fk_status_product = models.ForeignKey (Status_Product, default = 1, verbose_name = "Status Product", on_delete = models.SET_DEFAULT)

	class Meta:
		verbose_name_plural = "Product"

	def __str__(self):
		return self.desc_product


##############################
####### Employee Models ######
##############################

class Access_Type (models.Model):
	pk_access_type = models.IntegerField(primary_key=True, verbose_name = "ID Access Type")
	desc_access_type = models.CharField(max_length=512, verbose_name = "Access Type", null=True)

	class Meta:
		verbose_name_plural = "Access Type"

	def __str__(self):
		return self.desc_access_type


class Position (models.Model):
	pk_position = models.IntegerField(primary_key=True, verbose_name = "ID Position")
	desc_position = models.CharField(max_length=512, verbose_name = "Position")

	class Meta:
		verbose_name_plural = "Position"

	def __str__(self):
		return self.desc_position


class City (models.Model):
	pk_city = models.IntegerField(primary_key=True, verbose_name = "ID City")
	desc_city = models.CharField(max_length=512, verbose_name = "City")
	desc_state = models.CharField(max_length=512, default = None, verbose_name = "State")
	desc_country = models.CharField(max_length=512, default = None, verbose_name = "Country")

	class Meta:
		verbose_name_plural = "City"

	def __str__(self):
		return self.desc_city


class Contract_Type (models.Model):
	pk_contract_type = models.IntegerField(primary_key=True, verbose_name = "ID Contract Type")
	desc_contract_type = models.CharField(max_length=512, verbose_name = "Contract Type")

	class Meta:
		verbose_name_plural = "Contract Type"

	def __str__(self):
		return self.desc_contract_type


class Vendor (models.Model):
	pk_vendor = models.IntegerField(primary_key=True, verbose_name = "ID Vendor")
	desc_vendor = models.CharField(max_length=512, verbose_name = "Vendor")

	class Meta:
		verbose_name_plural = "Vendor"

	def __str__(self):
		return self.desc_vendor


class Status_Employee (models.Model):
	pk_status_employee = models.IntegerField(primary_key=True, verbose_name = "ID Status Employee")
	desc_status_employee = models.CharField(max_length=512, verbose_name = "Status Employee")

	class Meta:
		verbose_name_plural = "Status Employee"

	def __str__(self):
		return self.desc_status_employee


class Employee (models.Model):
	pk_employee = models.IntegerField(primary_key=True, verbose_name = "ID Employee")
	code_employee = models.IntegerField(verbose_name = "Employee Code")
	desc_employee = models.CharField(max_length=512, verbose_name = "Employee")
	fk_user = models.OneToOneField(User, default = None, verbose_name = "Username", on_delete=models.SET_DEFAULT, blank=True, null=True)
	fk_access_type = models.ForeignKey (Access_Type, default = 1, verbose_name = "Access Type", on_delete = models.SET_DEFAULT)
	fk_position = models.ForeignKey (Position, default = 1, verbose_name = "Position", on_delete = models.SET_DEFAULT)
	fk_employee_leader = models.ForeignKey ('self', default = None, verbose_name = "Leader", on_delete = models.SET_DEFAULT, blank=True, null=True)
	fk_city = models.ForeignKey (City, default = 1, verbose_name = "City", on_delete = models.SET_DEFAULT)
	fk_contract_type = models.ForeignKey (Contract_Type, default = 1, verbose_name = "Contract Type", on_delete = models.SET_DEFAULT)
	fk_vendor = models.ForeignKey (Vendor, default = 1, verbose_name = "Vendor", on_delete = models.SET_DEFAULT)
	fk_status_employee = models.ForeignKey (Status_Employee, default = 1, verbose_name = "Status Employee", on_delete = models.SET_DEFAULT)
	fk_cost_center = models.ForeignKey (Cost_Center, default = 1, verbose_name = "Cost Center", on_delete = models.SET_DEFAULT)
	date_admission = models.DateField(verbose_name = "Admission Date")
	date_termination = models.DateField(verbose_name = "Termination Date", blank=True, null=True, default=None)
	fk_employee_replacing = models.ForeignKey ('self', default = None, verbose_name = "Replacing", related_name = 'replacing', on_delete = models.SET_DEFAULT, blank=True, null=True)
	fk_employee_replaced_by = models.ForeignKey ('self', default = None, verbose_name = "Replaced By", related_name = 'replaced_by', on_delete = models.SET_DEFAULT, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Employee"

	def __str__(self):
		return self.desc_employee