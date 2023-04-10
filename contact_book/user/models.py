from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    Address = models.CharField(max_length=128)
    mobile = models.IntegerField(null=True)
    email = models.EmailField()
    password = models.CharField(max_length=2000)

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = []
    # objects = UserManager()

    def __str__(self):
        return self.email

class Contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)

class Mobile(models.Model):
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE)
    mobile = models.IntegerField()