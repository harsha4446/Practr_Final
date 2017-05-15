from django import forms
from users.models import round_scores


class assessmentForm(forms.ModelForm):
    class Meta:
        model = round_scores
        fields = ['question1','question2','question3','question4','question5','creativity',
                  'content','presentation','communication','rebuttal','feasibility','feedback']