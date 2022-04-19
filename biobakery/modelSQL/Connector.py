#!/usr/bin/env python3

"""


"""

__author__ = 'Bart Engels'
__data__ = '2019-12-05'
__version__ = 'v1-d2019'

import sys
import mysql.connector
from mysql.connector import errorcode
import argparse


class MysqlConnect:
    '''
    MysqlModules connect met een database door middel van een .my.cnf file of via het
    mee geven van de inlog gegeven in de terminal.
    '''
    try:
        def __init__(self, my_cnf, username, host, databasename, passwd, param, t_f):
            """

            :param my_cnf:
            :param username:
            :param host:
            :param databasename:
            :param passwd:
            """
            if my_cnf is None:
                self.connector = mysql.connector.connect(
                    host=host,
                    user=username,
                    database=databasename,
                    password=passwd
                )
            else:
                self.connector = mysql.connector.connect(
                    option_files=my_cnf)
            self.dbname = databasename
            self.cursor = self.connector.cursor()
            self.param = param
            self.trfa = t_f

    except TypeError:
        pass

    def connect_mysql(self):
        """
        Connect with mysql and checked if there are anny errors
        if there are errors this function will return this in a print function.
        """
        try:
            self.connector
            print('Connection is complete.... ', '\n')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Something is wrong with your username or password')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Database does not exist')
            elif err.errno == errorcode.ER_ACCESS_DENIED_NO_PASSWORD_ERROR:
                print('No password!!')
            else:
                print(err)


def main(args):
    inp_args = argparse.ArgumentParser()

    inp_args.add_argument('-c', '--cnf_file', help='hier kan een my.cnf file worden gebruikt om in te loggen. ')
    inp_args.add_argument('-u', '--username', help='vul de user naam van de data base in'
                                                   ' bij een localhost db kan "root" gebruikt worden.')
    inp_args.add_argument('-l', '--host', help='vul hier de host waar de database op draait.')
    inp_args.add_argument('-d', '--databasename', help='vul de naam van de database die je wil '
                                                       'gebruiken in.')
    inp_args.add_argument('-ps', '--password', help='vul hier het wachtwoord wat behoord '
                                                    'bij de usernaam en de database.')
    inp_args.add_argument('-pa', '--parameter', help='vul hier het oligo_id van de '
                                                     'sequentie die veranderd moet worden.')
    inp_args.add_argument('-tf', '--truefalse', help='vul hier in of de sequentie uniek is of niet. '
                                                     'doormiddel van een 1[true] of 0[false]')

    args = inp_args.parse_args()
    cnf_file = args.cnf_file
    username = args.username
    host = args.host
    databasename = args.databasename
    passwd = args.password
    param = args.parameter
    t_f = args.truefalse

    mysql_con = MysqlConnect(cnf_file, username, host, databasename, passwd, param, t_f)
    mysql_con.connect_mysql()

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
