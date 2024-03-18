from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,Group
from django.contrib.auth.models import PermissionsMixin,Permission
from django.forms import ValidationError


class ContactUs(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
        
# python manage.py dumpdata main.Services --output main/fixtures/Services.test.json

def upload_to(obj,filename):
    base_filename = os.path.basename(filename)
    file_name, file_extension = os.path.splitext(base_filename)
    return f"services/{obj.title}-{obj.index}{file_extension}"  
  


class Services(models.Model):
    title = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True,blank=True)
    # icon=models.CharField(max_length=50)
    icon=models.ImageField(upload_to=upload_to)
    index=models.IntegerField(default=1)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Services"


# python manage.py dumpdata main.Company --output main/fixtures/Company.test.json
class Company(models.Model):
    about = models.TextField()
    address = models.TextField()
    phone=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField()
    def clean(self):
        if Company.objects.exists() and not self.pk:
            raise ValidationError("You can only have one settings instance")
            
    def __str__(self):
        return f"{self.pk}"
    
    class Meta:
        verbose_name_plural = "Company"

# python manage.py dumpdata main.SocialLinks --output main/fixtures/SocialLinks.test.json

class SocialLinks(models.Model):
    name = models.CharField(max_length=100,unique=True,default="facebook")
    icon = models.CharField(max_length=100,default="fab fa-facebook",unique=True,)
    url=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Social Links"


class UserAccountManager(BaseUserManager):
    use_in_migrations = True
    

    def create_user(self, username,email, password=None):
        if not username:
            raise ValueError("Username invalid")
        if not email:
            raise ValueError("Email invalid")

        user = self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password):
        user = self.create_user(username=username,email=email,password=password)
        # user.is_active = True
        # user.is_admin = True
        # user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



import os
def upload_to(obj,filename):
    base_filename = os.path.basename(filename)
    file_name, file_extension = os.path.splitext(base_filename)
    return f"slider/{obj.types}-{obj.index}{file_extension}"


CHOICES_COLORS = [
        ('text-main', 'Green'),
        ('text-black', 'Black'),
        ('text-white', 'White'),
]
CHOICES_TYPES = [
        ('video', 'video'),
        ('image', 'image'),
]
class Slider(models.Model):
    title = models.CharField(max_length=100,unique=True,null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    # icon=models.CharField(max_length=50)
    image=models.FileField(upload_to=upload_to)
    index=models.IntegerField(default=1)
    text_color=models.CharField(max_length=20,choices=CHOICES_COLORS,default="text-black")
    types=models.CharField(max_length=20,choices=CHOICES_TYPES,default="image")

    def __str__(self):
        return f"slider-{self.pk}"
    
    class Meta:
        verbose_name_plural = "Slider"



# python manage.py dumpdata users.user --output users/fixtures/users.test.json
class User(AbstractBaseUser, PermissionsMixin):
    """ BmUser model """
    username=models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=250, unique=True,null=True,blank=True)
    password = models.CharField(max_length=250,null=True,blank=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now_add=True,null=True,blank=True)
    is_staff = models.BooleanField(default=False,null=True,blank=True)    # admin
    is_enabled = models.BooleanField(default=True,null=True,blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password',]

    objects = UserAccountManager()

    def __str__(self):
        return f"{self.email}"
  
    
    def has_module_perms(self, app_label):
        return True

    class Meta:
        ordering = ['id']
