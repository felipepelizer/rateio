from django.shortcuts import render, redirect
from .models import Business, Department, Company, Cost_Center, Allocation_Type, Status_Cost_Center
from .models import Status_Product, Segment, Product
from .forms import Cost_Center_Form, Product_Form
from django.db.models import Max


def home(request):
	return render (request, 'home.html', {})


#############################
##### Cost Center Views #####
#############################


def cost_center(request):
	cost_center_list = Cost_Center.objects.all()
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
####### Teste Views #######
#############################