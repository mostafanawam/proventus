from django.contrib import admin

from main.forms import CustomUserCreationForm
from .models import *

class ServicesAdmin(admin.ModelAdmin):  
    list_display = ("id","title",'icon')
admin.site.register(Services,ServicesAdmin)


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


