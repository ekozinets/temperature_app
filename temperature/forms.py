from django import forms
from .models import City
from bootstrap_datepicker_plus.widgets import DatePickerInput

class TemperatureChartForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all().order_by('name'))
    date = forms.DateField(
        widget = DatePickerInput(format='%d.%m.%Y'),
        input_formats = ('%d.%m.%Y', )
    )

class TemperatureFilterForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all().order_by('name'), required=False)
    date = forms.DateField(
        widget = DatePickerInput(format='%d.%m.%Y'),
        input_formats = ('%d.%m.%Y', ),
        required = False
    )
