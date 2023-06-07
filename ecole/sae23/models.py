# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Absence(models.Model):
    idabsence = models.SmallAutoField(primary_key=True)
    justifier = models.TextField(blank=True, null=True)  # This field type is a guess.
    justification = models.CharField(max_length=5000, blank=True, null=True)
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE, db_column='etudiant', blank=True, null=True)
    cours = models.ForeignKey('Cours', on_delete=models.CASCADE, db_column='cours', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'absence'

class Cours(models.Model):
    idcours = models.SmallAutoField(primary_key=True)
    titre_cours = models.CharField(max_length=40, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    duree = models.TimeField(blank=True, null=True)
    enseigant = models.ForeignKey('Enseigant', on_delete=models.CASCADE, db_column='enseigant', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cours'

class Enseigant(models.Model):
    idenseignant = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=40, blank=True, null=True)
    prenom = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enseigant'


class Etudiant(models.Model):
    idetudiant = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=40, blank=True, null=True)
    prenom = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    photo = models.ImageField(upload_to="ecole/", null=True)
    groupe = models.ForeignKey('Groupe', on_delete=models.CASCADE, db_column='groupe', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'etudiant'


class Groupe(models.Model):
    idgroupe = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'groupe'
