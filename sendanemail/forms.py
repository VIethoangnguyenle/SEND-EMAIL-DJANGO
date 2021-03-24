from django import forms

class SendEmail(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email

class SendMessage(forms.Form):
    Message = forms.Field()
    def __str__(self):
        return self.Message

class Subject(forms.Form):
    Sub = forms.Field()
    def __str__(self):
        return self.Sub