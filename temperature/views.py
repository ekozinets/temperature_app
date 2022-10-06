from django.views import generic
from django.http import JsonResponse
from .models import CityTemperature 
from .forms import TemperatureChartForm, TemperatureFilterForm

class ChartFormView(generic.FormView):
    template_name = 'main_form.html'
    form_class = TemperatureChartForm

    def form_invalid(self, form):
        return JsonResponse({'error': True, 'error': form.errors})

    def form_valid(self, form):
        city = form.cleaned_data['city']
        date = form.cleaned_data['date']
        labels = []
        data = []
        queryset = CityTemperature.objects.all().filter(
            city = city,
            date__year = date.year,
            date__month = date.month,
            date__day = date.day
        ).order_by('date')
        for city_temperature in queryset:
            labels.append(city_temperature.date.strftime('%H:%M'))
            data.append(city_temperature.temperature_value)
        
        return JsonResponse(data = {
            'success': True,
            'labels': labels,
            'data': data,
        })


class TemperatureListView(generic.ListView):
    template_name = 'list_view.html'
    paginate_by = 10
    model = CityTemperature
    context_object_name = 'temperature_list'

    def get_context_data(self, **kwargs):
        context = super(TemperatureListView, self).get_context_data(**kwargs)
        context['form'] = TemperatureFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('date')
        form = TemperatureFilterForm(self.request.GET)
        if (form.is_valid()):
            city = form.cleaned_data['city']
            if (city):
                queryset = queryset.filter(city=city)
            date = form.cleaned_data['date']
            if (date):
                queryset = queryset.filter(
                    date__year = date.year,
                    date__month = date.month,
                    date__day = date.day
                )
        return queryset
