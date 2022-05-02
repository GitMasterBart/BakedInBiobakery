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
        self.intials = "beng"
        self.department = "microbio"
        self.research = "intitials_datum_departmen_onderzoek"

    def parse_tsv_file(self):
        with open(self.file) as myfile:
            head = [next(myfile) for x in range(10)]
        for i in range(len(head)):
            print(head[int(i) -1][0:19])

    def add_to_db(self):
        Researches.objects.create("")


        print(Users.objects.all())

def main():
    WriteToDb().parse_tsv_file()

if __name__ == '__main__':
    main()