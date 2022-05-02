#!/env/bin/python3

import mysql
from django.conf import settings
from mysql.connector import connect

import django, os

os.environ["DJANGO_SETTINGS_MODULE"] = "djangoProject.settings"
django.setup()

from django.conf import settings
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

    def __init__(self):
        self.file = "/Users/bengels/Desktop/output_data/output_gentable.tsv"
        self.intials = "BENG"
        self.department = "Microbiologie"
        self.research = "intitials_datum_departmen_onderzoek"

    def parse_tsv_file(self):
        with open(self.file) as myfile:
            head = [next(myfile) for x in range(10)]
            for i in myfile:
                # print(head[int(i) -1][0:19])

                print(i.split(" ")[1].split("\t"))


    def add_research_to_db(self):
        user_id = Users.objects.filter(initials=self.intials).values_list('User_id', flat=True).first()
        department_id = Department.objects.filter(name=self.department).values_list('department_id', flat=True).first()
        Researches.objects.create(name=self.research, department_id=department_id, user_id_id=user_id)





def main():
    WriteToDb().parse_tsv_file()

if __name__ == '__main__':
    main()