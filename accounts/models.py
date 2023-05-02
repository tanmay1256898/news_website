from django.db import models
from django.db import connections
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    description = models.TextField()
    date = models.DateField()
    class Meta:
        db_table='contact'
    def __str__(self):
        return self.name


class categore(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    link= models.URLField()
    description = models.TextField()
    def __str__(self):
        return self.link
    class Meta:
        db_table='categore'
    
class zeenews(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    link= models.URLField()
    description = models.TextField()
    def __str__(self):
        return self.link
    class Meta:
        db_table='zeenews'
    
class cricketlivescore(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    link= models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.link
    class Meta:
        db_table='cricketlivescore'