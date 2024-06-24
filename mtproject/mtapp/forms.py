

from django import forms

from mtapp.models import Emp,Student






class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields="__all__"
        
class StudForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"