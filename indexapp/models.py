from django.db import models


class rca(models.Model):
    file = models.FileField(upload_to="obradeni_excel/", max_length=250)

    def __str__(self):
        return self.title

class gliit(models.Model):
    file = models.FileField(upload_to="obradeni_excel/", max_length=250)
    
    def __str__(self):
        return self.title

class tfcc(models.Model):
    file = models.FileField(upload_to="obradeni_excel/", max_length=250)
    
    def __str__(self):
        return self.title

class ci(models.Model):
    file = models.FileField(upload_to="obradeni_excel/", max_length=250)
    
    def __str__(self):
        return self.title

class svi(models.Model):
    file = models.FileField(upload_to="obradeni_excel/", max_length=250)
    
    def __str__(self):
        return self.title


