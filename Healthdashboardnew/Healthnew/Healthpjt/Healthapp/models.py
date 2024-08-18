from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

#for main treemap
class diseasestreemap(models.Model):
    Disease_ID = models.IntegerField(_("Diseases_ID"))
    Disease_Name = models.CharField(_("Disease_Name"),max_length=250)
    Disease_Type = models.CharField(_("Disease_Type"),max_length=250)
    DALYRate = models.IntegerField(_("DALYRate"))
    def __str__(self):
        return self.Disease_Name

## for servicetreemap
class Disease(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='services')
    def __str__(self):
        # Return a string representation that includes relevant information
        return f"{self.name} - {self.value} for Disease: {self.disease.name}"


class Servicenew(models.Model):
    servicename = models.CharField(max_length=100)
    subservice = models.CharField(max_length=100)
    value = models.IntegerField()
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='servicenew')
    def __str__(self):
        # Return a string representation that includes relevant information
        return f"{self.servicename} - {self.value} for Disease: {self.disease.name}"


class Subservicenew(models.Model):
    subservice = models.CharField(max_length=100)
    directinpts = models.CharField(max_length=100)
    resources = models.CharField(max_length=100)
    value = models.IntegerField()
    def __str__(self):
        return f"{self.subservice}"

class Subservice(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name