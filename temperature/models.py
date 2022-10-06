from datetime import datetime
from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError

class City(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'cities'
        ordering = ['name']


class CityTemperature(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateTimeField('date measured')
    temperature_value = models.IntegerField(default=0)

    @admin.display(description='Temperature')
    def temperature_str(self):
        temperature_str = ''
        if self.temperature_value > 0:
            temperature_str = '+{0}°C'.format(self.temperature_value)
        else:
            temperature_str = '{0}°C'.format(self.temperature_value)
        return temperature_str

    def __str__(self):
        return '{0} - {1} {2}'.format(
            self.city.name,
            self.date.strftime('%d.%m.%Y %H:%M'),
            self.temperature_str()
        )

    def validate_unique(self, exclude=None):
        queryset = CityTemperature.objects.filter(
            city = self.city,
            date__year = self.date.year,
            date__month = self.date.month,
            date__day = self.date.day,
            date__hour = self.date.hour
        )
        if queryset.exists() and self.pk != queryset[0].pk:
            raise ValidationError('Data already exists for this City and hour')
        return super(CityTemperature, self).validate_unique(exclude=exclude)

    def save(self, *args, **kwargs):
        self.date = datetime(self.date.year, self.date.month, self.date.day, self.date.hour)
        super(CityTemperature, self).save(*args, **kwargs)
    
    class Meta:
        db_table = 'city_temperatures'
        ordering = ['date']
        unique_together = ('city', 'date')
