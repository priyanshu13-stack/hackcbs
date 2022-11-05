from django.db import models
class resume(models.Model):
    name = models.CharField(max_length= 200, default='', unique=True)
    contact = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200, default='' , unique=True)
    about_me = models.CharField(max_length=200, default='')
    career_objective = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name
