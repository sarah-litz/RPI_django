from django import forms 
from .models import Experiment, Script

class ExperimentForm(forms.ModelForm): 
    class Meta: 
        model = Experiment
        fields = ['user_name']
        labels = {'user_name':'user_name'}


class ScriptForm(forms.ModelForm): 
    class Meta: 
        model = Script
        fields = ['type']
        labels = {'type':'type'}
        # experiment = Experiment.objects.latest('date')
        # script = forms.ModelMultipleChoiceField(queryset=Experiment.)