from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicatonForm(forms.Form):
    CHOICES = [('human', 'HUMAnN3'), ('phyloplan', 'PhyloPhlAn3') ,('metaplan', 'metaphlan3')]
    BiobakeryTool = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    project = forms.CharField()
    date = forms.DateField(widget=DateInput)
    input_file = forms.FileField()
