from django.db import models
import os

import djangoProject


class Department(models.Model):
    name = models.CharField(max_length=15)
    department_id = models.AutoField(primary_key=True)

    # researches = models.ManyToManyField(Researches.researches_id,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Users(models.Model):
    initials = models.CharField(max_length=4)
    departments = models.ManyToManyField(Department)
    User_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.initials


class Researches(models.Model):
    name = models.CharField(max_length=50)
    researches_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.PROTECT)
    user_id = models.ForeignKey(Users, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class DumpTable(models.Model):
    gene = models.CharField(max_length=25)
    family = models.CharField(max_length=50)
    sample = models.CharField(max_length=60)
    result = models.IntegerField()
    researches_id = models.ForeignKey(Researches, blank=True, null=True, on_delete=models.PROTECT)
    user_id = models.ForeignKey(Users, blank=True, null=True, on_delete=models.PROTECT)
