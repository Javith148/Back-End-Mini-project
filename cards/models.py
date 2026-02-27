from django.db import models

class addImage(models.Model):
   
    image = models.ImageField(upload_to='cards/')
    title = models.CharField(max_length=400, default='Untitled')
    des = models.CharField(max_length=2000 ,default='Untitled')

    def __str__(self):
        return self.title

class SendOtp(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

    



    


