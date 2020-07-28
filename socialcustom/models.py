# from django.db import models
# from django.db.models import CharField
# # Create your models here.
# class User(models.Model):
#     Username = models.CharField(max_length=128 , unique=False)
#     email = models.EmailField(max_length=254)
#     password = models.CharField(max_length=10)
#     # password2 = models.CharField(max_length=12)


from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Profile1(models.Model) :
    Username = models.CharField(max_length=30)
    Biography = models.CharField(max_length= 260)
    image = models.ImageField(upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    # address = models.CharField(max_length=255)
    # address2 =models.CharField(max_length=244)
    # city = models.CharField(max_length=255)
    # # state = models.CharField(max_length=255)
    # zip = models.IntegerField()


class Profile2(models.Model):
        # Username = models.CharField(max_length=30)
        # Biography = models.CharField(max_length=260)
        first_name = models.CharField(max_length=255)
        last_name = models.CharField(max_length=255)
        email = models.CharField(max_length=255)
        address = models.CharField(max_length=255)
        address2 =models.CharField(max_length=244)
        city = models.CharField(max_length=255)
        state = models.CharField(max_length=255)
        zip = models.IntegerField()

