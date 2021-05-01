from django.db import models

# Create your models here.
class Inputab(models.Model):
    date_posted=models.DateTimeField(auto_now_add=True)
    first=models.TextField()
    last=models.TextField()
    report=models.TextField()
    phone=models.IntegerField()
    email=models.TextField()
    address=models.TextField()
    address2=models.TextField()
    state=models.TextField()
    state_zip=models.IntegerField()
    date_posted=models.DateTimeField(auto_now_add=True)

class current_position(models.Model):
    location=models.TextField()   
    date_posted=models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return 'Entry #{}'.format(self.id)  

 