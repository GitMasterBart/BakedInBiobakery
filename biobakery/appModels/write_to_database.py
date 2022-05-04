#!/env/bin/python3

"""
This class pushes the result data in a database, it uses django
models to make contact with the mysql database. It is a class that needs five variables:
 file, initials, department, date, research_name
"""

import time
import os
from django.conf import settings
from django.db.utils import DataError
import django
import pandas as pd


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

from biobakery.models import *

class WriteToDb:
    """
    WritTodb is a class that contains 4 classes to write data to a database,
    this database is set in the setting from this djangoproject. further is each methode named
    after the data that is parses. : (add_Users_to_db, add_department_to_db,
    add_research_to_adb, add_results_to_db )
    """

    def __init__(self, file, initials, department, date, research_name):
        self.file = file
        self.initials = initials
        self.department = department
        self.research = research_name + "_" + date + "_" + initials

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

    def add_results_to_db(self):
        """
        Adds all te result with the samples to a database if they doe not already exists.
        :return: if DataError: str("Datapoints already exists.")
        """
        if DumpTable.objects.filter(researches_id_id=self.research_id,
                                    user_id_id=self.user_id).exists():
            return exit(DataError)
        try:
            transformed_table = pd.DataFrame(pd.melt(pd.read_table(self.file, lineterminator='\n'),
                                                     id_vars="# Gene Family"))
            for i in range(transformed_table.size):
                gene = transformed_table.values[i][0].split(" ")[0][0:19]
                if len(transformed_table.values[i][0].split(' ')) == 2:
                    family = transformed_table.values[i][0].split(' ')[1]
                else:
                    family = '\t'
                sample = str(transformed_table.values[i][1])
                result = transformed_table.values[i][2]
                DumpTable.objects.create(gene=gene, family=family, sample=sample, result=result,
                                             researches_id_id=self.research_id,
                                             user_id_id=self.user_id)
        except DataError:
            return "Datapoints already exists."


def main():
    start = time.process_time()
    createdb = WriteToDb("/Users/bengels/Desktop/output_data/output_gentable.tsv",
                         "beng", "Microbiologie",
                         "2022-05-03", "FirstTestOnderzoek")
    createdb.add_users_to_db()
    createdb.add_research_to_db()
    createdb.add_results_to_db()
    stop = time.process_time()
    with open("/Users/bengels/Desktop/output_data/new.txt", "w") as new_file:
        new_file.write("Elapsed time during the whole program in seconds: {} "
                       .format(str(stop - start)))


if __name__ == '__main__':
    main()
