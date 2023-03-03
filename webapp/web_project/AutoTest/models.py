from django.db import models

class accounts(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

class testS(models.Model):  
    scenario = models.CharField(max_length=500)
    output = models.CharField(max_length=500)
    report = models.CharField(max_length=500)

class sourceC(models.Model):  
    upload = models.FileField(upload_to ='uploads/')
    output = models.CharField(max_length=500)
    report = models.CharField(max_length=500)


class const(models.Model):  
    const = models.CharField(max_length=500)

