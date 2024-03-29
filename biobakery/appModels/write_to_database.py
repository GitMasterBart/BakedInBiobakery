#!/env/bin/python3

"""
This class pushes the result data in a database, it uses django
models to make contact with the mysql database. It is a class that needs five variables:
 file, initials, department, date, research_name
"""

import os
from django.conf import settings
from django.db.utils import DataError
import django


os.environ["DJANGO_SETTINGS_MODULE"] = "djangoProject.settings"
django.setup()

if not settings.configured:
    settings.configure(
        # DATABASE_ENGINE = 'django.db.backends.mysql',
        # DATABASE_NAME = 'biobakery',
        # DATABASE_USER = 'root',
        # DATABASE_PASSWORD = 'rakker444',
        # DATABASE_HOST = '127.0.0.1',
        # DATABASE_PORT = '3306',
    )

from biobakery.models import Users, Department, Researches


class WriteToDb:
    """
    WritTodb is a class that contains 4 classes to write data to a database,
    this database is set in the setting from this djangoproject. further is each methode named
    after the data that is parses. : (add_Users_to_db, add_department_to_db,
    add_research_to_adb, add_results_to_db )
    """

    def __init__(self, initials, department, research_name):

        self.initials = initials
        self.department = department
        self.research = research_name

        self.user_id = Users.objects.filter(initials=self.initials) \
            .values_list('User_id', flat=True).first()
        self.department_id = Department.objects.filter(name=self.department) \
            .values_list('department_id', flat=True).first()
        self.research_id = Researches.objects.filter(name=self.research) \
            .values_list('researches_id', flat=True).first()

    def add_users_to_db(self):
        """
        Adds a user to database if it does not already exists.
        :return if DataError : str with "Datapoint already exists."
        """
        try:
            if not Users.objects.filter(initials=self.initials).exists():
                Users.objects.create(initials=self.initials)
        except DataError:
            return "Datapoint already exists."

    def add_department_to_db(self):
        """
        Adds a department to database if it does not already exists.
        :return: if DataError: str("Datapoint already exists.")
        """
        try:
            if not Department.objects.filter(name=self.department).exists():
                Department.objects.create(name=self.department)
        except DataError:
            return "Datapoint already exists."

    def add_research_to_db(self):
        """
        Adds research to database if it does not already exists.
        :return: if DataError: str("Datapoint already exists.")
        """
        try:
            if not Researches.objects.filter(name=self.research, department_id=self.department_id,
                                             user_id_id=self.user_id).exists():
                Researches.objects.create(name=self.research, department_id=self.department_id,
                                          user_id_id=self.user_id)
                self.research_id = Researches.objects.filter(name=self.research) \
                    .values_list('researches_id', flat=True).first()
        except DataError:
            return "Datapoint already exists."
