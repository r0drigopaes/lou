__author__ = 'Rodrigo Paes - rodrigo@ic.ufal.br'

import codecs
import csv


def read_csv(path_to_file, lines_to_ignore):
    csvfile = codecs.open(path_to_file, "r", encoding='utf-8', errors='ignore')

    csvreader = csv.reader(csvfile, delimiter=';')
    returned_value = []
    i = 0
    for row in csvreader:
        if i < lines_to_ignore:
            i += 1
        else:
            returned_value.append(row)
    return returned_value