from django.db import models


class Itineraire(models.Model):
    titre = models.CharField(max_length=200)
    point_de_depart = models.CharField(max_length=200)
    description = models.TextField(default="")
    altitude_de_depart =  models.IntegerField('altitude (m)')
    altitude_min = models.IntegerField('altitude (m)')
    altitude_max = models.IntegerField('altitude (m)')
    denivele_positif_cumule = models.FloatField(default=0)
    denivele_negatif_cumule = models.FloatField(default=0)
    duree_estimee = models.FloatField('Duree estimee (h)')
    difficulte_estimee = models.IntegerField('Difficulte')
    def __str__(self):
        return self.titre

class sortie(models.Model):
    utilisateur = models.CharField(max_length=200)
    itineraire = models.ForeignKey('Itineraire', on_delete=models.CASCADE) 
    date_de_sortie = models.DateTimeField('date de sortie')
    duree_reelle = models.FloatField('Duree reelle (h)')
    nombre_de_personne = models.IntegerField('le nombre de personnes ayant participe à la sortie')
    experience = models.CharField(max_length=200)
    meteo = models.CharField(max_length=200)
    difficulte = models.IntegerField('la difficulté ressentie')
    commentaire= models.TextField(default="");
    def __str__(self):
        return self.utilisateur