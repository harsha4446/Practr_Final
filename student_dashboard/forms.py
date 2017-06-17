from django import forms
from users.models import round_scores, event_registered_details

class dataForm(forms.ModelForm):
    data1 = forms.FileField(label='File 1',required=True,widget=forms.FileInput({'placeholder':'teting'}))
    data2 = forms.FileField(label='File 2',required=False)
    data3 = forms.FileField(label='File 3',required=False)
    class Meta:
        model = round_scores
        fields = ['data1','data2','data3']

class detailFrom(forms.ModelForm):

    class Meta:
        model = event_registered_details
        fields = ['marketing','best_manager','finance','ent_dev','public_relations',
                  'human_resources',]
