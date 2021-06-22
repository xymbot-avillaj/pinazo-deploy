from .models import Production
from django.forms import ModelForm, DateTimeInput


class DateTimeInput(DateTimeInput):
    input_type = "datetime-local"
    #input_type = "datetime"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)

class ProductionForm(ModelForm):    
    class Meta: 
        model = Production
        fields = {'article', 'machine', 'total', 'date_from', 'date_to'}
        widgets = {                      
            'date_from': DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),
            'date_to': DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),
        }