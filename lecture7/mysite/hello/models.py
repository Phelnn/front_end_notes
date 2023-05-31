from django.db import models

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
    

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")  #ForeignKey用于跟机场关联, related_name用于提供访问关联类(Airport)这个属性的接口
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):   #添加这个查询返回函数后需要quit()再重新python manage.py shell, from hello.models import Flight, 再Flight.objects.all()才会有相应效果
        return f"{self.id} - {self.origin} to {self.destination}"
    
