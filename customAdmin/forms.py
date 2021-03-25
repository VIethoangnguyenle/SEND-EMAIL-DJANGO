from django import forms
from customAdmin.models import PersonalInfor

class InputName(forms.Form):
    Name = forms.Field()
    def __str__(self):
        return self.Name

class InputEmail(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email

class InputLevel(forms.Form):
    Level = forms.ChoiceField(choices=PersonalInfor.LEVEL_CHOICES)
    def __str__(self):
        return self.Level

class InputAge(forms.Form):
    Age = forms.IntegerField(initial=0)
    def __str__(self):
        return self.Age

class InputSubject(forms.Form):
    Subject = forms.Field()
    def __str__(self):
        return self.Subject