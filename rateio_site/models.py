from django.db import models

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