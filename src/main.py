from cryptanalysis import CryptAnalysis
from utils import arbitary_mapping_sub


FROMPATH = '../data/challenge-2-ct.txt'

MOSTALPHA = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l',
                  'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k',
                  'j', 'x', 'q', 'z']

class Main(object):
    def __init__(self, source_data, turn_name):
        self.source_data = source_data
        self.turn_name = turn_name
        self.chars_list = None
        self.enc_data = None
        
    def exec_analysis(self):
        """execute analysis"""
        crypt = CryptAnalysis(self.source_data)
        for i in range(1, 4):
            crypt.exec(i, self.turn_name + '-' + str(i) + 'freq.csv')
            if i == 1:
                self.chars_list = crypt.chars
                self.enc_data = crypt.encrypted_data

    def exec_sub(self, _map_dict):
        """execution"""
        arbitary_mapping_sub(self.enc_data, _map_dict, self.turn_name + '-sub.txt')
       
if __name__ == '__main__':
    c2 = Main(FROMPATH, 'c2')
    c2.exec_analysis()
    map_dict_guess_1 = dict(zip(c2.chars_list, MOSTALPHA))
    c2.exec_sub(map_dict_guess_1)
