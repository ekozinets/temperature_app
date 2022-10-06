from django.contrib import admin
from .models import City, CityTemperature

@admin.register(CityTemperature)
class CityTemperatureAdmin(admin.ModelAdmin):
    list_display = ('city', 'show_date', 'show_hour', 'temperature_str')
    list_filter = ('city', 'date')
    list_per_page = 15
    date_hierarchy = 'date'
    ordering = ('-date',)

    @admin.display(description='Date')
    def show_date(self, obj):
        return obj.date.strftime('%d.%m.%Y')

    @admin.display(description='Hour')
    def show_hour(self, obj):
        return obj.date.strftime('%H:%M')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_per_page = 15

