"""execute analysis and substitution"""
from cryptanalysis import CryptAnalysis
from utils import arbitary_mapping_sub
from utils import read_file_from

MOSTALPHA = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l',
                  'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k',
                  'j', 'x', 'q', 'z']

class Main(object):
    """functions"""
    def __init__(self, turn_name, from_path_file):
        # self.source_data = '../data/' + source_data
        self.turn_name = turn_name
        self.chars_list = None
        self.enc_data = read_file_from('../data/' + from_path_file)
        
    def exec_analysis(self, encrypted_data):
        """execute analysis"""
        crypt = CryptAnalysis(encrypted_data)
        # analysis frequency of 1 char, 2 chars and 3 chars
        for i in range(1, 4):
            crypt.exec(i, self.turn_name + '-' + str(i) + 'freq.csv')
            if i == 1:
                self.chars_list = crypt.chars

    def exec_sub(self, map_dict):
        """execute substitution and return sub_path"""
        sub_path = '../data/' + self.turn_name + '-sub.txt'
        arbitary_mapping_sub(self.enc_data, map_dict, sub_path)
        return sub_path

def execution(dict_change, name, source_file):
    """execute substitution result and anaylsis it"""
    inst = Main(name, source_file) # Instantiate the Main class
    _subp = inst.exec_sub(dict_change) # execute substitution
    _subp_data = read_file_from(_subp)
    inst.exec_analysis(_subp_data) # execute analysis


if __name__ == '__main__':
    # c2 = Main('c2')
    # c2.exec_analysis('challenge-2-ct.txt')
    dict_all = {'µ':'t', '¬':'h', '©':'e', 'Ω':'o', '¡':'z', 'ç':'q', 'å':'a', '÷':'w', 'ß':'b','∂':'c', '†':'k', '≥':'u', '∆':'f', '√':'r', '˚':'g', '∫':'s', '®':'l', '≠':'y', 'π':'i', 'œ':'n', '≤':'v', '«':'x', 'ƒ':'d', '∑':'m', '≈':'p', 'ø':'j'}
    execution(dict_all, '12all', 'challenge-2-ct.txt')
    