from django import forms
from users.models import round_scores, event_registered_details

class dataForm(forms.ModelForm):
    data1 = forms.FileField(required=True,)
    data2 = forms.FileField(required=False)
    data3 = forms.FileField(required=False)
    class Meta:
        model = round_scores
        fields = ['data1','data2','data3']

class detailFrom(forms.ModelForm):
    class Meta:
        model = event_registered_details
        fields = ['marketing','best_manager','finance','ent_dev','public_relations',
                  'human_resources',]
