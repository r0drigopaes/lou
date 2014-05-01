__author__ = 'Rodrigo Paes - rodrigo@ic.ufal.br'

import codecs
import csv


def read_csv(path_to_file):
    csvfile = codecs.open(path_to_file, "r", encoding='utf-8', errors='ignore')

    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        if len(row)>2:
            print(row[1])