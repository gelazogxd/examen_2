# from django.contrib.auth.models import User
# from django.db import models

# # Create your models here.

# class City(models.Model):
#     id = models.IntegerField(primary_key=True)
#     ciudad = models.CharField(max_length=128, null=True)

# class Stadium(models.Model):
#     num = models.IntegerField(primary_key=True, default=0)
#     nombre = models.CharField(max_length=128, default='20')  # Establece una cadena vacía como valor predeterminado
#     description = models.CharField(max_length=256, default='30')

#     def __str__(self):
#         return self.nombre



# class Team(models.Model):
#     codigo = models.IntegerField(primary_key=True, default=0)
#     equipo = models.CharField(max_length=128, null=True)
#     liga = models.CharField(max_length=256, null=True)

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class City(models.Model):
#     ciudad = models.CharField(max_length=128, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'City'


# class Stadium(models.Model):
#     num = models.AutoField(primary_key=True)
#     estadio = models.IntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=128, blank=True, null=True)
#     description = models.CharField(max_length=256, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Stadium'


# class Team(models.Model):
#     codigo = models.AutoField(primary_key=True)
#     equipo = models.CharField(max_length=128, blank=True, null=True)
#     liga = models.CharField(max_length=256, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Team'

from django.db import models


class City(models.Model):
    id = models.AutoField(primary_key=True)  #
    ciudad = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'City'


class Stadium(models.Model):
    num = models.AutoField(primary_key=True)
    estadio = models.IntegerField(blank=True, null=True)  # Agrega este campo
    nombre = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Stadium'



class Team(models.Model):
    codigo = models.AutoField(primary_key=True)
    equipo = models.CharField(max_length=128, blank=True, null=True)
    liga = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Team'

class Relationship(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


    def __str__(self):
        return f'Relationship {self.id}'
    