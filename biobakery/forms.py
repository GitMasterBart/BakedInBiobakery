from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicatonForm(forms.Form):
    CHOICES = [('1', 'HUMAnN3'), ('2', 'PhyloPhlAn3') ,('3', 'metaphlan3')]
    BiobakeryTool = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    project = forms.CharField()
    date = forms.DateField(widget=DateInput)
    input_file = forms.FileField()




#
# class UserForm(forms.Form):
#     first_name= forms.CharField(max_length=100)
#     last_name= forms.CharField(max_length=100)
#     email= forms.EmailField()
