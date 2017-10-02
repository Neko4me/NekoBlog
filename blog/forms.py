from django import forms
from .models import Messge
class MessForm(forms.ModelForm):
    class Meta:
        model=Messge
        fields=['name','text']
        labels={'text':'Text','name':'Name'}
        widgets={'text':forms.Textarea(attrs={'cols':80})}