from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicatonForm(forms.Form):
    TOOL_CHOICES = [('human', 'HUMAnN3') ] #, ('phyloplan', 'PhyloPhlAn3') , ('metaplan', 'metaphlan3')]
    BiobakeryTool = forms.ChoiceField(widget=forms.RadioSelect, choices=TOOL_CHOICES)
    KNEADDATA_OPTIONS = [("~/Desktop/Uploaded_files/humann_dbs/silvadb/", "silvadatabase"),
                         ("~/Desktop/kneaddataMap/Trimmomatic-0.36/","trimmomatic"),
                         ("--bypass-trf","bypass_trf"),
                         ("--run-fastqc-start","fastqc_start"),
                         ("--run-fastqc-end","fastqc_end")]
    HUMAN_OPTIONS = [("--bypass-nucleotide-search", "bypass_n_search"),
                         ("--remove-temp-output","remove_temp_output"),
                         ("--verbose","verbose"),
                         ("~/Desktop/Uploaded_files/humann_dbs/unireffull/","protein_db"),
                         ("/Users/bengels/Desktop/Uploaded_files/humann_dbs/chocophlan","nucleotide_db")]
    tool_optons_kneaddata = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=KNEADDATA_OPTIONS)
    tool_optons_humann = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=HUMAN_OPTIONS)
    project = forms.CharField(max_length=15)
    date = forms.DateField(widget=DateInput)
    # unlock = forms.ChoiceField(widget=forms.CheckboxInput)
    input_file = forms.FileField()

class NewUserForm(forms.Form):
    initials = forms.CharField(max_length=4)