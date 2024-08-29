from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rang"
        verbose_name_plural = "Ranglar"


class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    date_manufactured = models.DateField()
    count = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Avtomobil"
        verbose_name_plural = "Avtomobillar"
