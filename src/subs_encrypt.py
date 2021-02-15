from utils import *
from cryptanalysis import CryptAnalysis

class Substitution(object):
    def __init__(self, pt_data, key, to_path):
        self.pt_data = pt_data
        self.new_alphabet = []
        self.key = key
        self.to_path = to_path

    def sub_mapping(self, key):
        new_alphabet = [''] * 26
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        for i in range(0, 26):
            new_alphabet[i] = alphabet[(i + key) % 26]

        dict_sub_map = dict(zip(alphabet, new_alphabet))
        return dict_sub_map
        

    def encryption(self):
        """execute encryption"""
        arbitary_mapping_sub(self.pt_data, self.sub_mapping(self.key), self.to_path)

    def analysis(self, to_path_csv):
        """execute analysis"""
        enc = read_file_from(self.to_path)
        cra = CryptAnalysis(enc)
        cra.exec(1, to_path_csv)
    
    def execution(self, to_path_csv):
        """execute encryption and analysis"""
        self.encryption()
        self.analysis(to_path_csv)

if __name__ == '__main__':
    pt = read_file_from('../data_subs/challenge-2-pt.txt')

    sub = Substitution(pt, 5, '../data_subs/c2-subs-ct.txt')
    sub.execution('../data_subs/c2-subs-analysis.csv')
        