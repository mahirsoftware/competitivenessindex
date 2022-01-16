from django import forms
from django.forms.fields import CharField, ChoiceField, FileField
from .fields import CommaSeparatedField
from .models import rca, gliit, tfcc, ci, svi     



class CreateTemplateForm(forms.Form):
    zemlja = forms.CharField(label='In order to get to the results you need to create an excel template where you will input data that you want to analyze. If you want to analyze multiple countries you will need to create multiple templates. In the first field (Country name), you need to input the name of the country that you want to analyze, also the name of the country will be the name of the Excel document. In the next field please input Country name (this is country that is focus of your research/analysis):')
    zemlje = CommaSeparatedField(label='In the second field, you need to input the names of trade partner countries and you need to separate them with commas. For every trading partner (country) in this field, will be created a new spreadsheet in the Excel document. Trade partners (these are the countries with which the "country" has a trade exchange):')
    godine = CommaSeparatedField(label='In the third field, you need to input years of trade. Every year, you need to separate with a comma. Years of trade:')
    tarife = CommaSeparatedField(label='In the fourth field, you need to input trade tariffs or sectors that you want to analyze. For every trade tariff or sector, you need to separate with a comma.')
    
class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')

########

class RCAForm(forms.ModelForm):
    class Meta:
        model = rca
        fields = ('file',)

class GLIITForm(forms.ModelForm):
    class Meta:
        model = gliit
        fields = ('file',)
    

class TFCCForm(forms.ModelForm):
    class Meta:
        model = tfcc
        fields = ('file',)
        
class CIForm(forms.ModelForm):
    class Meta:
        model = ci
        fields = ('file',)

class SVIForm(forms.ModelForm):
    class Meta:
        model = svi
        fields = ('file',)

class ColorfulContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your name here'
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={'style': 'border-color: green;'})
    )
    subject = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;'
            }
        )
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
        help_text='Write here your message!'
    )


