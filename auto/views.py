from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import BrandForm, ColorForm, CarForm
from .models import Brand, Color, Car
from django.contrib import messages


class DashboardView(View):
    def get(self, request):
        brands = Brand.objects.all()
        colors = Color.objects.all()
        cars = Car.objects.all()
        brand_form = BrandForm()
        color_form = ColorForm()
        car_form = CarForm()
        context = {
            'title': 'Bosh sahifa',
            'brands': brands,
            'colors': colors,
            'cars': cars,
            'brand_form': brand_form,
            'color_form': color_form,
            'car_form': car_form,
        }
        return render(request, 'dashboard.html', context)


class CreateBrandView(View):
    def post(self, request):
        form = BrandForm(request.POST)
        if form.is_valid():
            form.create()
            messages.success(request, "Brend qo'shildi!")
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

        return redirect('dashboard')

    def get(self, request):
        return redirect('dashboard') # agar get so'rov kelsa bosh sahifaga qaytarib yuboradi


class UpdateBrandView(View):
    def post(self, request, id):
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = Brand.objects.get(pk=id)
            form.update(brand=brand)
            messages.success(request, "Brend yangilandi!")
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

        return redirect('dashboard')

    def get(self, request, id):
        return redirect('dashboard')


class DeleteBrandView(View):
    def get(self, request, id):
        try:
            Brand.objects.get(id=id).delete()
            messages.warning(request, "Brend o'chirildi!")
        except:
            messages.error(request, "Qandaydur xatolik yuz berdi!")

        return redirect('dashboard')


class CreateColorView(View):
    def post(self, request):
        form = ColorForm(request.POST)
        if form.is_valid():
            form.create()
            messages.success(request, "Rang qo'shildi!")
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")
        return redirect('dashboard')

    def get(self, request):
        return redirect('dashboard')


class UpdateColorView(View):
    def post(self, request, id):
        form = ColorForm(request.POST)
        if form.is_valid():
            color = Color.objects.get(pk=id)
            form.update(color=color)
            messages.success(request, "Rang yangilandi!")
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")
        return redirect('dashboard')

    def get(self, request, id):
        return redirect('dashboard')


class DeleteColorView(View):
    def get(self, request, id):
        try:
            Color.objects.get(pk=id).delete()
            messages.warning(request, "Rang o'chirildi!")
        except:
            messages.error(request, "Qandaydur muammo yuz berdi!")
        return redirect('dashboard')


class CreateCarView(View):
    def get(self, request):
        return redirect('dashboard')

    def post(self, request):
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, "Avtomobil qo'shildi!")
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")
        return redirect('dashboard')


class UpdateCarView(View):
    def get(self, request, id):
        return redirect('dashboard')

    def post(self, request, id):
        car = get_object_or_404(Car, pk=id)
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            car_form.update(car)
            messages.success(request, "Avtomobil ma'lumotlari yangilandi!")
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")
        return redirect('dashboard')


class DeleteCarView(View):
    def get(self, request, id):
        try:
            Car.objects.get(pk=id).delete()
            messages.warning(request, "Avtomobil o'chirildi!")
        except:
            messages.error(request, "Qandaydur muammo yuz berdi!")
        return redirect('dashboard')
