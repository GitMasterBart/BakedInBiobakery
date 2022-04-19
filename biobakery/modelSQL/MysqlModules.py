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
from biobakery.modelSQL.Connector import MysqlConnect

class MysqlModules:
    '''
    MysqlModules connect met een database door middel van een .my.cnf file of via het
    mee geven van de inlog gegeven in de terminal en bevat 3 modules die
    ieder stored routine bevatten:
    sp_get_genes: voert een sql quary uit die de data uit de genen tabel haalt.
    sp_get_tm_vs_probes: voert een sql query uit die data uit oligos tabel haalt.
    '''

    def __init__(self, cnf_file, username, host, databasename, passwd, param, t_f):
        mysql_con = MysqlConnect(cnf_file, username, host, databasename, passwd, param, t_f)
        mysql_con.connect_mysql()
        self.param = param
        self.trfa = t_f
        self.cursor = self

    def sp_get_genes(self):
        """

        :return:
        """
        print('#' * 100, "\n")
        try:
            form_m = ''
            query = 'sp_get_genes'
            print('Gen data in dit sql file: \n')
            print("\tgen_id  | gen")
            self.cursor.callproc(query)
            l_gen = self.cursor.stored_results()
            for result in l_gen:
                results = result.fetchall()
                for r in results:
                    form_m += """\t{} | {} \n""". format(r[0], r[1])
                return form_m
        except mysql.connector.errors.ProgrammingError:
            return 'De tabel is niet aanwezig in de database {}'.format(self)

    def sp_get_tm_vs_probes(self):
        """

        :return:
        """
        try:
            print('#' * 100, "\n")
            self.cursor.callproc('sp_get_tm_vs_probes')
            div_smelt_oli = self.cursor.stored_results()
            for results in div_smelt_oli:
                results = results.fetchall()
                print("Het aantal verschillende smelttemperaturen gedeeld door het aantal oligo's")
                for dec in results:
                    dec = float(str(dec)[10:16])
                    return 'smelttempratuur/oligos : {}\n'.format(dec)
        except mysql.connector.errors.ProgrammingError:
            return 'De tabel is niet aanwezig in deze database. DBnaam: {}'.format(self.dbname)

    def sp_mark_duplicate_oligos(self):
        """

        :return:
        """
        form_o = ""
        print('#' * 100, "\n")
        self.cursor.callproc('sp_mark_duplicate_oligos', (self.param, self.trfa,))
        self.cursor.stored_results()
        self.cursor.execute("select * from oligos")
        n_table = self.cursor.fetchall()
        print("Oligo nulceotide information: ")
        print('\toligo_id | gene_id | oligos | gc_perc | smelttempratuur | uniek')
        for oli_result in n_table:
            form_o += """\t  {} | {} | {} | {} | {} | {} \n  """.format(oli_result[0], oli_result[1], oli_result[2],
                                                                        oli_result[3], oli_result[4], oli_result[5])
        return form_o



def main(args):
    """

    :return:
    """

    inp_args = argparse.ArgumentParser()

    inp_args.add_argument('-c', '--cnf_file', help='hier kan een my.cnf file worden gebruikt om in te loggen. ')
    inp_args.add_argument('-u', '--username', help='vul de user naam van de data base in'
                                                   ' bij een localhost db kan "root" gebruikt worden.')
    inp_args.add_argument('-l','--host', help='vul hier de host waar de database op draait.')
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


    print('#' * 100, "\n")
    input_data = input('Welke data moet er worden getoond?\n'
                       '*Voor het aantal verschillende smelttemperaturen gedeeld door het '
                       'aantal oligos, gebruik: gvsp\n'
                       '*Voor de gen data, gebruik: geninfo\n'
                       '*voor de oligo data, gebruik: oligoD\n\n'
                       'vul in: ')

    if input_data == 'geninfo':
        print(mysql_con.sp_get_genes())
        vv_info = input("meer info?: ")
        if vv_info == "y":
            main(args)
        else:
            SystemExit
    elif input_data == 'gvsp':
        print(mysql_con.sp_get_tm_vs_probes())
        vv_info = input("meer info?: ")
        if vv_info == "y":
            main(args)
        else:
            SystemExit
    elif input_data == 'oligoD':
        print(mysql_con.sp_mark_duplicate_oligos())
        vv_info = input("meer info?: ")
        if vv_info == "y":
            main(args)
        else:
            SystemExit
    else:
        print("\nOeps...... ik vermoed een typefout. ")
        try_again = input('probeer opnieuw, ok? y[yes] or n[no] : ')
        if try_again == 'y':
            main(args)
        else:
            raise SystemExit

if __name__ == '__main__':
    sys.exit(main(sys.argv))
