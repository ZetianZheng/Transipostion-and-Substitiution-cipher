from utils import *
from cryptanalysis import CryptAnalysis

class VigenereCipher(object):
    def __init__(self, key_size, enc_data):
        self.key_size = key_size
        self.enc_data = enc_data

    def split(self):
        """split ct to n strings, stored in a list"""
        split_list = [''] * self.key_size
        for i in range(len(self.enc_data)):
            split_list[i % self.key_size] += self.enc_data[i] 
        return split_list

    def split_to_files(self, split_list, to_path):
        for i, temp_str in enumerate(split_list):
            temp_str = split_list[i]
            write_data_to(to_path + 'set'+ str(i + 1) + '.txt', temp_str)
            self.analysis(temp_str, to_path + 'set'+ str(i + 1) + 'freq.csv')

        print('split done! all files and frequency anaylsis been stored in:' + to_path)
    
    def exec(self, to_path):
        temp_list = self.split()
        self.split_to_files(temp_list, to_path)

    def analysis(self, enc_data, to_path):
        c_a = CryptAnalysis(enc_data)
        c_a.exec(1, to_path)


if __name__ == '__main__':
    vc = VigenereCipher(5, read_file_from('../data_vigenere/vigenere_ct.txt'))
    vc.exec('../data_vigenere/')
            