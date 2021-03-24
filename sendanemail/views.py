from django.shortcuts import render
from django.http import HttpResponse
from EmailSMTP.settings import EMAIL_HOST_USER
from django.core.mail import send_mail,send_mass_mail
from . import forms
# Create your views here.

def SendEmail(request):
    sub = forms.SendEmail()
    message = forms.SendMessage()
    subject = forms.Subject()
    if request.method == 'POST':
        sub = forms.SendEmail(request.POST)
        subject = forms.Subject(request.POST)
        message = forms.SendMessage(request.POST)

        subj = str(subject['Sub'].value())
        mes  = str(message['Message'].value())
        recepient = str(sub['Email'].value())

        send_mail(subj,mes,EMAIL_HOST_USER,[recepient],fail_silently=False)
        return render(request,'sendanemail/success.html',{'recepient':recepient})
    return render(request,'sendanemail/index.html',{'form':sub, 'mes':message,'subject':subject})
