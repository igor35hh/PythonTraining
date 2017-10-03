from django import forms

def validate_file_extension(value):
        if not value.name.endswith('.csv'):
            raise forms.ValidationError("Only CSV file is accepted")

class UploadFileForm(forms.Form):
    filename = forms.FileField(widget=forms.FileInput(attrs={'accept': ".csv"}), validators=[validate_file_extension])
    
    