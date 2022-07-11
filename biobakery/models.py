"""
Models.py holds the structure for creating a database, if changes are made, the command:
`migrate` and `make-migrate` must be executed.
"""

from django.db import models


class Department(models.Model):
    """
    structure of the department table.
    a name of the department with an id, (auto incremented)
    """
    name = models.CharField(max_length=15)
    department_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.name)


class Users(models.Model):
    """
        structure of the Users table.
        an initial of the user with an id, (auto incremented) and the department they work for.
    :return: string `initials`
    """
    initials = models.CharField(max_length=4)
    departments = models.ManyToManyField(Department)
    User_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.initials)


class Researches(models.Model):
    """
    structure of the researches table
    contains name of the research corresponding department. and user id of the user that
    did the analysis.
    autoincrement id of research
    """
    name = models.CharField(max_length=50)
    researches_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.PROTECT)
    user_id = models.ForeignKey(Users, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)


class DumpTable(models.Model):
    """
    structure of dumptable table, with the fields gene, family, sample, results
    research id and user id.
    """
    gene = models.CharField(max_length=100)
    family = models.CharField(max_length=150)
    sample = models.CharField(max_length=100)
    result = models.FloatField()
    researches_id = models.ForeignKey(Researches, blank=True, null=True, on_delete=models.PROTECT)
    user_id = models.ForeignKey(Users, blank=True, null=True, on_delete=models.PROTECT)
