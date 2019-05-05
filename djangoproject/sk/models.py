from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name



class Picture(models.Model):
    pic = models.FileField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
