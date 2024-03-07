from django.urls import path
from .views import  *

app_name = "main"
urlpatterns = [
    path('',main_page, name='main_page'),
    path('contact-us/',contactUs, name='contactUs'),
    path('test/',test_page, name='test'),

]
