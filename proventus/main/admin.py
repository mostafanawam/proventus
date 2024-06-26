from django.contrib import admin

from main.forms import CustomUserCreationForm
from .models import *

class ServicesAdmin(admin.ModelAdmin):  
    list_display = ("id","title",'icon','index')
admin.site.register(Services,ServicesAdmin)

class ContactUsAdmin(admin.ModelAdmin):  
    list_display = ("id","name","email","subject")
admin.site.register(ContactUs,ContactUsAdmin)



class SocialLinksAdmin(admin.ModelAdmin):  
    list_display = ("id","name",'icon','url')
admin.site.register(SocialLinks,SocialLinksAdmin)


class SliderAdmin(admin.ModelAdmin):  
    list_display = ("id","title",'text','index','types','text_color')
admin.site.register(Slider,SliderAdmin)

class CompanyAdmin(admin.ModelAdmin):  
    list_display = ("id","address",'phone',"register_number","email")
admin.site.register(Company,CompanyAdmin)


admin.site.unregister(Group)
class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    fields = [
        'email','password','is_staff','is_superuser','is_enabled'
    ]
    list_display = (
        'id',
        'email',
        'is_staff',
        'is_enabled',
        'is_superuser',
        'last_login',
    ) 
    list_filter = ('is_staff',)
admin.site.register(User, UserAdmin)


