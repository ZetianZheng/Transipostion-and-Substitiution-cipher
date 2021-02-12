""" step 2, get frequency analysis to pairs chars"""
from utils import *

DATAPATH2 = '../data/c2-decrypt-1.txt'
ANSPATH2 = '../data/results2.csv'

def number_2_statistics(_encrypted_data):
    """ return a number of all different 2 length words
    the dict of that and numbers of a pair chars"""
    dict_char = {}
    count = 0
    temp_list = []
    for i in range(0, len(_encrypted_data) - 1):
        temp_list.append(_encrypted_data[i])
        temp_list.append(_encrypted_data[i + 1])
        temp_str = "".join(temp_list)
        if temp_str in dict_char:
            dict_char[temp_str] += 1
        else:
            dict_char[temp_str] = 1
        temp_list = []
        count += 1
    return count, dict_char

def main2():
    """ execution function"""
    encrypted_data = read_file_from(DATAPATH2)
    count, dict_chars = number_2_statistics(encrypted_data)
    chars, numbers, frequencies = statistics_analysis(dict_chars, count)
    write_to_csv(chars, numbers, frequencies, ANSPATH2)

if __name__ == '__main__':
    main2()
    print('step 2 done')