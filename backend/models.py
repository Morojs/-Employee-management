from django.db import models

# Create your models here.
from datetime import date

class Foncion(models.Model):
    nom = models.CharField(max_length=50, null=False)
    rtt=models.IntegerField(null=False)

class Service(models.Model):
    nom=models.CharField(max_length=50,null=False)
    rtt=models.IntegerField(null=False)

class Employe(models.Model):
    nom = models.CharField(max_length=25, null=False)
    prenom = models.CharField(max_length=25, null=False)
    date_naissance = models.DateTimeField(auto_now_add=False,default=date.today, null=False)
    date_embauche = models.DateTimeField(auto_now_add=True, null=False)

    fonction = models.ForeignKey(Foncion, null=True,on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True,on_delete=models.CASCADE)

class Salaire(models.Model):
        date_debut = models.DateTimeField(auto_now_add=False,default=date.today, null=False)
        date_fin = models.DateTimeField(auto_now_add=False,default=date.today, null=False)
        chargepatronales = models.FloatField( null=False)
        charge_salariales = models.FloatField(null=False)
        sal_brut=models.FloatField(null=False)
        employe=models.ForeignKey(Employe,null=False,on_delete=models.CASCADE)


class Conge(models.Model):
        date_debut = models.DateTimeField(auto_now_add=False,default=date.today,null=False)
        date_fin = models.DateTimeField(auto_now_add=False,default=date.today,null=False)
        employe=models.ForeignKey(Employe,null=False,on_delete=models.CASCADE)

