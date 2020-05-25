from django import forms
from .models import Busines

class BusinesForm(forms.ModelForm):
    class Meta:
        model = Busines
        fields = ['Category', 'Location', 'BusinessName', 'Email', 'Password', 'Telephone']