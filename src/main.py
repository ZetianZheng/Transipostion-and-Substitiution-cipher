from cryptanalysis import Crypt1Analysis
from substitution import Substituion
from cryptanalysis2 import Crypt2Analysis
from cryptanalysis3 import Crypt3Analysis

FROMPATH = '../data/challenge-2-ct.txt'

MOSTALPHA = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l',
                  'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k',
                  'j', 'x', 'q', 'z']
class main(object):
    def __init__(self, source_data, turn_name):
        self.source_data = source_data
        self.turn_name = turn_name
        self.chars_list = []
        self.enc_data = ''
        self.exec_analysis()

    def exec_analysis(self):
        crypt1 = Crypt1Analysis(self.source_data, self.turn_name + '-1freq.csv')
        Crypt2Analysis(self.source_data, self.turn_name + '-2freq.csv')
        Crypt3Analysis(self.source_data, self.turn_name + '-3freq.csv')
        self.chars_list = crypt1.chars
        self.enc_data = crypt1.encrypted_data

    def exec_sub(self, _map_dict):
        """execution"""
        Substituion(self.enc_data, _map_dict, self.turn_name + '-sub.txt')
        # anaylsis pair chars
       
if __name__ == '__main__':
    c2 = main(FROMPATH, 'c2')
    map_dict_guess_1 = dict(zip(c2.chars_list, MOSTALPHA))
    c2.exec_sub(map_dict_guess_1)
