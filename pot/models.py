from django.db import models
from django.contrib.auth import get_user_model



User=get_user_model()

# Create your models here.
class Plant(models.Model):
    plant_name = models.CharField(max_length=50,default="Unknow plant")
    alarm = models.TimeField(null = True)
    humidity = models.FloatField(default=0) 
    threadhold = models.IntegerField(default=0)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"<Plant {self.plant_name} by {self.customer}>"


class History_Pest(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    pest_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.pest_name
        
    
class History_Water(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)    
    

  