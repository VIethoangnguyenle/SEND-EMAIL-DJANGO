from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from . import forms
from django.utils.html import strip_tags
from EmailSMTP.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.core.mail import send_mail
from customAdmin.models import PersonalInfor
# Create your views here.
def Register(request):
    #Initialize variables
    name = forms.InputName()
    age = forms.InputAge()
    level = forms.InputLevel()
    mail = forms.InputEmail()
    subject = forms.InputSubject()
    if request.method =='POST':

        #Get data from user
        name = forms.InputName(request.POST)
        age = forms.InputAge(request.POST)
        level = forms.InputLevel(request.POST)
        mail = forms.InputEmail(request.POST)
        subject = forms.InputSubject(request.POST)
        
        #Get string
        name = str(name['Name'].value())
        age = str(age['Age'].value())
        level = str(level['Level'].value())
        mail = str(mail['Email'].value())
        subject = str(subject['Subject'].value())

        #Add database
        PersonalInfor.objects.create(name=name, age=age, level=level, email= mail).save()
        
        html_message = render_to_string('customAdmin/message.html',{'name':name,'age':age,'level':level,'mail':mail})
        plain_message = strip_tags(html_message)
        
        send_mail(subject,plain_message,EMAIL_HOST_USER,[mail],html_message=html_message)        
        return render(request,'customAdmin/success.html',{'mail':mail,'name':name,'age':age,'level':level})
    return render(request,'customAdmin/main.html',{'name':name,'age':age,'level':level,'mail':mail,'subject':subject})

