from django.shortcuts import render, redirect
from .models import Car
from .forms import Creating_carForm, CarForm
from django.contrib import messages

def car_list(request):

	context = {
		"cars": Car.objects.all()
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	form = Creating_carForm()
	if request.method == 'POST':
		form = Creating_carForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('car-list')


	context = {
	'form' : form
	}
	return render(request, 'car_create.html', context)


def car_update(request, car_id):
	form_obj = Car.objects.get(id=car_id)
	form = CarForm(instance=form_obj)
	if request.method == 'POST':
		form = CarForm(request.POST, request.FILES or None, instance=form_obj)
		if form.is_valid():
			form.save()
			messages.success(request, 'Profile details updated.')
			# return redirect('car-list')
	context = {
	'form_obj': form_obj,
	'form': form
	}
	return render(request, 'car_update.html', context)

def car_delete(request, car_id):
	Car.objects.get(id=car_id).delete()
	return redirect('car-list')
