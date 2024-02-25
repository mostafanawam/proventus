from django.contrib import admin

from main.forms import CustomUserCreationForm
from .models import *

class ServicesAdmin(admin.ModelAdmin):  
    list_display = ("id","title",'icon','index')
admin.site.register(Services,ServicesAdmin)



class SocialLinksAdmin(admin.ModelAdmin):  
    list_display = ("id","name",'icon','url')
admin.site.register(SocialLinks,SocialLinksAdmin)



class CompanyAdmin(admin.ModelAdmin):  
    list_display = ("id","address",'phone',"email")
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


