from django.shortcuts import render, redirect
from django.db.models import Max
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Business, Department, Company, Cost_Center, Allocation_Type, Status_Cost_Center
from .models import Status_Product, Segment, Product
from .models import Access_Type, Position, City, Contract_Type, Vendor, Status_Employee, Employee
from .models import Squad_Group, Status_Squad, Squad
from .forms import Cost_Center_Form, Product_Form, Sign_Up_Form, Employee_Form, Squad_Form
from .serializers import Cost_Center_Serializer


class Cost_Center_View(viewsets.ModelViewSet):
    serializer_class = Cost_Center_Serializer
    queryset = Cost_Center.objects.all()




def home(request):
	return render (request, 'home.html', {})


#############################
##### Cost Center Views #####
#############################

def cost_center(request):
	cost_center_list = Cost_Center.objects.all().exclude(desc_cost_center='Undefined')
	return render (request, 'cost_center.html', {'cost_center_list': cost_center_list})


def cost_center_create (request):
	if request.method == 'POST':
		form = Cost_Center_Form(request.POST)

		if form.is_valid():
			form.save()
			return redirect ('cost_center')

	cost_center_next_pk = Cost_Center.objects.aggregate(Max('pk_cost_center'))['pk_cost_center__max'] + 1
	form = Cost_Center_Form(initial = {'pk_cost_center': cost_center_next_pk})
	return render (request, 'cost_center_create.html', {'form': form})


def cost_center_edit(request, id):
	cost_center = Cost_Center.objects.get(pk_cost_center=id)
	if request.method == 'POST':
		form = Cost_Center_Form(request.POST, instance = cost_center)

		if form.is_valid():
			form.save()
			return redirect ('cost_center')
		
	form = Cost_Center_Form(initial = {	'pk_cost_center': cost_center.pk_cost_center,
										'code_cost_center': cost_center.code_cost_center,
										'desc_cost_center': cost_center.desc_cost_center,
										'fk_department': cost_center.fk_department,
										'fk_business': cost_center.fk_business,
										'fk_company': cost_center.fk_company,
										'fk_allocation_type': cost_center.fk_allocation_type,
										'fk_status_cost_center': cost_center.fk_status_cost_center,})
	return render (request, 'cost_center_edit.html', {'form': form, 'id': id})


def cost_center_delete (request, id):
	cost_center = Cost_Center.objects.get(pk_cost_center=id)
	cost_center.delete()
	return redirect('cost_center')


#############################
####### Product Views #######
#############################

def product(request):
	product_list = Product.objects.all()
	return render (request, 'product.html', {'product_list': product_list})


def product_create (request):
	if request.method == 'POST':
		form = Product_Form(request.POST)

		if form.is_valid():
			form.save()
			return redirect ('product')

	product_next_pk = Product.objects.aggregate(Max('pk_product'))['pk_product__max'] + 1
	form = Product_Form(initial = {'pk_product': product_next_pk})
	return render (request, 'product_create.html', {'form': form})


def product_edit(request, id):
	product = Product.objects.get(pk_product=id)
	if request.method == 'POST':
		form = Product_Form(request.POST, instance = product)

		if form.is_valid():
			form.save()
			return redirect ('product')
		
	form = Product_Form(initial = {	'pk_product': product.pk_product,
									'desc_product': product.desc_product,
									'fk_segment': product.fk_segment,
									'fk_status_product': product.fk_status_product,})
	return render (request, 'product_edit.html', {'form': form, 'id': id})


def product_delete (request, id):
	product = Product.objects.get(pk_product=id)
	product.delete()
	return redirect('product')


#############################
######## User Views #########
#############################

def login_user (request):
	if request.method == 'POST':
		username = request.POST['teste']
		password = request.POST ['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect ('home')
		else:
			return redirect ('login')
	else:
		return render (request, 'login.html', {})


def logout_user (request):
	logout(request)
	return redirect ('home')


def register_user(request):
	if request.method == 'POST':
		form = Sign_Up_Form(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			return redirect ('home')
	else:
		form = Sign_Up_Form()
	return render (request, 'register.html', {'form': form})



#############################
####### Employee Views ######
#############################

def employee(request):
	employee_list = Employee.objects.all()
	return render (request, 'employee.html', {'employee_list': employee_list})


def employee_create (request):
	if request.method == 'POST':
		form_user = Sign_Up_Form(request.POST)
		form_employee = Employee_Form(request.POST)

		if form_employee.is_valid() and form_user.is_valid(): 
			form_user.save()
			form_employee.save()
			Employee.objects.filter(pk_employee=form_employee.cleaned_data['pk_employee']).update(fk_user=form_user.save())
			return redirect ('employee')

	employee_next_pk = Employee.objects.aggregate(Max('pk_employee'))['pk_employee__max'] + 1
	form_employee = Employee_Form(initial = {'pk_employee': employee_next_pk})
	form_user = Sign_Up_Form()
	return render (request, 'employee_create.html', {'form_employee': form_employee, 'form_user': form_user})


def employee_edit(request, id):
	employee = Employee.objects.get(pk_employee=id)
	if request.method == 'POST':
		form_employee = Employee_Form(request.POST, instance = employee)

		if form_employee.is_valid():
			form_employee.save()
			return redirect ('employee')
		
	form_employee = Employee_Form(initial = {	'pk_employee': employee.pk_employee,
												'code_employee': employee.code_employee,
												'desc_employee': employee.desc_employee,
												'fk_user': employee.fk_user,
												'fk_access_type': employee.fk_access_type,
												'fk_position': employee.fk_position,
												'fk_employee_leader': employee.fk_employee_leader,
												'fk_city': employee.fk_city,
												'fk_contract_type': employee.fk_contract_type,
												'fk_vendor': employee.fk_vendor,
												'fk_status_employee': employee.fk_status_employee,
												'fk_cost_center': employee.fk_cost_center,
												'date_admission': employee.date_admission,
												'date_termination': employee.date_termination,
												'fk_employee_replacing': employee.fk_employee_replacing,
												'fk_employee_replaced_by': employee.fk_employee_replaced_by,})

	return render (request, 'employee_edit.html', {'form_employee': form_employee, 'id': id})


def employee_delete (request, id):
	employee = Employee.objects.get(pk_employee=id)
	employee.delete()
	return redirect('employee')


#############################
######## Squad Views ########
#############################

def squad(request):
	squad_list = Squad.objects.all()
	return render (request, 'squad.html', {'squad_list': squad_list})


def squad_create (request):
	if request.method == 'POST':
		form = Squad_Form(request.POST)

		if form.is_valid():
			form.save()
			return redirect ('squad')

	squad_next_pk = Squad.objects.aggregate(Max('pk_squad'))['pk_squad__max'] + 1
	form = Squad_Form(initial = {'pk_squad': squad_next_pk})
	return render (request, 'squad_create.html', {'form': form})


def squad_edit(request, id):
	squad = Squad.objects.get(pk_squad=id)
	if request.method == 'POST':
		form = Squad_Form(request.POST, instance = squad)

		if form.is_valid():
			form.save()
			return redirect ('squad')
		
	form = Squad_Form(initial = {	'pk_squad': squad.pk_squad,
									'desc_squad': squad.desc_squad,
									'fk_squad_group': squad.fk_squad_group,
									'fk_status_squad': squad.fk_status_squad,})
	return render (request, 'squad_edit.html', {'form': form, 'id': id})


def squad_delete (request, id):
	squad = Squad.objects.get(pk_squad=id)
	squad.delete()
	return redirect('squad')