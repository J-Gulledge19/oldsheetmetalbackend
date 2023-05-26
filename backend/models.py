from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20, unique=True)
    number = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.name
    
class Download(models.Model):
    dlName = models.CharField(max_length=50)
    done = models.BooleanField()
    dateTurnedIn = models.CharField(max_length=10)
    active = models.BooleanField()
    class weight: 
        galv = models.IntegerField()
        ss = models.IntegerField()
        blackIron = models.IntegerField()
        pl = models.IntegerField()
        alum = models.IntegerField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='downloads')
    
    def __str__(self):
        return self.dlName