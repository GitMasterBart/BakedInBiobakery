"""
This file holds the structure for all the forms that are present in this application.
"""

from django import forms
import Pathways


class DateInput(forms.DateInput):
    """
      a class that containts all the objects that are pressent in the date form
    """
    input_type = 'date'


class ApplicatonForm(forms.Form):
    """
    a class that containts all the objects that are pressent in the application form
    """
    TOOL_CHOICES = [('human', 'HUMAnN3') ]
    BiobakeryTool = forms.ChoiceField(widget=forms.RadioSelect, choices=TOOL_CHOICES)
    KNEADDATA_OPTIONS = [(Pathways.LOCATIONSILVADATABASE, "silvadatabase"),
                         (Pathways.LOCATIONTRIMMOMATICDATABASE, "trimmomatic"),
                         ("--bypass-trf","bypass_trf"),
                         ("--run-fastqc-start","fastqc_start"),
                         ("--run-fastqc-end","fastqc_end")]
    HUMAN_OPTIONS = [("--bypass-nucleotide-search", "bypass_n_search"),
                     ("--remove-temp-output","remove_temp_output"),
                     ("--verbose","verbose"),
                     (Pathways.LOCATIONUNIREFFPULLDATABASE, "protein_db"),
                     (Pathways.LOCATIONCHOCOPHLANDATABASE, "nucleotide_db")]
    tool_optons_kneaddata = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                      choices=KNEADDATA_OPTIONS)
    tool_optons_humann = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                   choices=HUMAN_OPTIONS)
    project = forms.CharField(max_length=15)
    date = forms.DateField(widget=DateInput)
    input_file = forms.FileField()


class NewUserForm(forms.Form):
    """
     a class that contains all the objects that are present in the new user form
    """
    initials = forms.CharField(max_length=4)
