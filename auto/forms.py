from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from .models import Brand, Color, Car


class BrandForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'brandName',
            }
        )
    )

    def create(self):
        brand = Brand.objects.create(name=self.cleaned_data['name'])
        return brand

    def update(self, brand):
        brand.name = self.cleaned_data['name']
        brand.save()
        return brand

class ColorForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'colorName',
            }
        )
    )

    def create(self):
        color = Color.objects.create(name=self.cleaned_data['name'])
        return color

    def update(self, color):
        color.name = self.cleaned_data['name']
        color.save()
        return color


class CarForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'carName',
            }
        )
    )
    color = forms.ModelChoiceField(
        queryset=Color.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'carColor',
            }
        )
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'carBrand',
            }
        )
    )
    date_manufactured = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'carDateManufactured',
            }
        )
    )
    count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'carCount',
            }
        )
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'carPrice',
            }
        )
    )

    class Meta:
        model = Car
        fields = ['name', 'color', 'brand', 'date_manufactured', 'count', 'price']

    def clean_date_manufactured(self):
        date_manufactured = self.cleaned_data.get('date_manufactured')
        if date_manufactured > date.today():
            raise ValidationError("Ishlab chiqarilgan sana bugungi kundan keyin bo'lishi mumkin emas.")
        return date_manufactured

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 1:
            raise ValidationError("Mashina narxi $1000 dan kam bo'lishi mumkin emas.")
        return price

    def clean_count(self):
        count = self.cleaned_data.get('count')
        if count < 1:
            raise ValidationError("Mashina narxi $1000 dan kam bo'lishi mumkin emas.")
        return count

    def update(self, car):
        car.name = self.cleaned_data.get('name')
        car.brand = self.cleaned_data.get('brand')
        car.color = self.cleaned_data.get('color')
        car.date_manufactured = self.cleaned_data.get('date_manufactured')
        car.count = self.cleaned_data.get('count')
        car.price = self.cleaned_data.get('price')
        car.save()
        return car
