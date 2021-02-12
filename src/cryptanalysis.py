"""computer securtiy arbitary mapping"""
from utils import *

MOSTALPHA = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l',
                  'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k',
                  'j', 'x', 'q', 'z']
DATAPATH = '../data/challenge-2-ct.txt'
ANSPATH = '../data/results.csv'

def number_statistics (_encrypted_data):
    """count each character, return number of chars and frequency dict"""
    dict_char = {}
    count = 0
    for i in _encrypted_data:
        if i in dict_char:
            dict_char[i] += 1
        else:
            dict_char[i] = 1
        count += 1

    return count, dict_char

def arbitary_mapping(_org_data, _enc_ranked_chars):
    """substitution to enctypt data"""
    Idx = [_ for _ in range(26)]
    chars_idx_dict = dict(zip(_enc_ranked_chars, Idx))

    decrypt_data = ""
    for _ in _org_data:
        _ = MOSTALPHA[chars_idx_dict[_]]
        decrypt_data += _
    write_data_to('../data/c2-decrypt-1.txt', decrypt_data)

def main():
    """read data from txt, do analysis and rank the chars, write the answer to csv"""
    encrypted_data = read_file_from(DATAPATH)
    count, dict_chars = number_statistics(encrypted_data)
    chars, numbers, frequencies = statistics_analysis(dict_chars, count)
    write_to_csv(chars, numbers, frequencies, ANSPATH)
    ### arbitary_mapping
    arbitary_mapping(encrypted_data, chars)

if __name__ == '__main__':
    main()
    print("done")
