from django.contrib import admin
from customAdmin.models import PersonalInfor
# Register your models here.
class AdminScreen(admin.ModelAdmin):
    pass

admin.site.register(PersonalInfor,AdminScreen)

