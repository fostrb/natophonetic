#!/usr/bin/python

import argparse
import sys
import os
from collections import OrderedDict
from stat import S_ISFIFO

ND = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliet",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-ray",
        "Y": "Yankee",
        "Z": "Zulu"
    }


def convert_character(input_character):
    if input_character.upper() in ND.keys():
        return ND[input_character.upper()]
    else:
        return input_character


def convert_word(input_word):
    output_list = []
    for character in input_word:
        c = convert_character(character)
        output_list.append(c)
    return output_list


def convert_list(in_list):
    greater_symbols_list = []
    for word in in_list:
        symbols = convert_word(word)
        greater_symbols_list.append(symbols)
    return greater_symbols_list


def convert_list_pretty(in_list):
    greater_symbols_dict = OrderedDict()
    for word in in_list:
        greater_symbols_dict[word] = convert_word(word)
    return greater_symbols_dict


def display_output(greater_list):
    for word_symbols in greater_list:
        for symbol in word_symbols:
            print(symbol)


def display_pretty_output(greater_dict):
    for word, symbols in greater_dict.items():
        print(word)
        for symbol in symbols:
            print("\t" + symbol)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Default for input is standard input for purposes of input piping.
    parser.add_argument("-i", "--input", nargs='*', help='<Required> Set flag', default=[])
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='defaults to standard in. For purposes of piping input.')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                        help='defaults to standard out. For purposes of piping output.')
    parser.add_argument('-p', '--pretty', action='store_true', default=False,
                        help='Pretty formatting of output.')

    args = parser.parse_args()

    input_list = []     # type: list

    if S_ISFIFO(os.fstat(0).st_mode):
        for each in args.infile:
            input_list += each.split()
    else:
        for arg in args.input:
            if os.path.isfile(arg):
                f = open(arg)
                file_data = f.readlines()
                f.close()
                for line in file_data:
                    input_list.append(line.strip())
            else:
                input_list.append(arg)

    if args.pretty:
        gsd = convert_list_pretty(input_list)
        display_pretty_output(gsd)
    else:
        gsl = convert_list(input_list)
        display_output(gsl)