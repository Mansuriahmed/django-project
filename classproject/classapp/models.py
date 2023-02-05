from django.db import models

# Create your models here.
class myUser(models.Model):
    Username=models.CharField(max_length=100,primary_key=True)
    Useraddress=models.CharField(max_length=100)

    def __str__(self):
        return self.Username

class Fooditem(models.Model):
    Foodname=models.CharField(max_length=100)
    Foodprice=models.IntegerField()

    def __str__(self):
        return self.Foodname

class Reviews(models.Model):
    Foodid=models.ForeignKey(Fooditem,on_delete=models.CASCADE)
    Reviewername=models.ForeignKey(myUser,on_delete=models.CASCADE)
    Rating=models.IntegerField()

