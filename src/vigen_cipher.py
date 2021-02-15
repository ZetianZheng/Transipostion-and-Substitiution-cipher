from utils import *
from cryptanalysis import CryptAnalysis

class VigenereCipher(object):
    """
    anaylsis Vigenere encrypt cipher, get plain text,
    Do encryption or Decryption using Vigenere algorihm
    """

    def __init__(self, enc_data, key_size = None):
        self.key_size = key_size
        self.enc_data = enc_data
        self.most_chars =[]
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def split(self):
        """split ct to n strings, stored in a list"""
        split_list = [''] * self.key_size
        for i in range(len(self.enc_data)):
            split_list[i % self.key_size] += self.enc_data[i]
        return split_list

    def split_to_files(self, split_list, to_path):
        """break the list, put each item to each file"""
        for i, temp_str in enumerate(split_list):
            temp_str = split_list[i]
            write_data_to(to_path + 'set'+ str(i + 1) + '.txt', temp_str)
            self.analysis(temp_str, to_path + 'set'+ str(i + 1) + 'freq.csv')

        print('split done! all files and frequency anaylsis been stored in:' + to_path)

    def exec_analysis(self, to_path):
        """execute analysis"""
        temp_list = self.split()
        self.split_to_files(temp_list, to_path)

    def analysis(self, enc_data, to_path):
        """
        analysis to splited data, write results to files and get most frequent letter from each split
        """
        c_a = CryptAnalysis(enc_data)
        c_a.exec(1, to_path)
        self.most_chars.append(c_a.chars[0]) # get most frequent letter

    def get_keys_from_analysis(self):
        """
        guess key list by assuming e is the most frequent letter in English
        """
        e_pos = self.alphabet.index('e')
        key_list = []
        for char in self.most_chars:
            dis = self.alphabet.index(char) - e_pos
            if dis < 0:
                dis += 26
            key_list.append(self.alphabet[dis])
        return key_list

    def get_new_char(self, char, key, mode = 'enc'):
        """get char as plain text or cipher text, return new char"""
        if mode == 'dec': # do decryption, char = CT
            index = self.alphabet.index(char) - self.alphabet.index(key)
        elif mode == 'enc': # do encryption, char = PT
            index = self.alphabet.index(char) + self.alphabet.index(key)
        else:
            print('undefined mode! please input enc or dec')
            return None
        if index < 0:
            index += 26
        if index > 25:
            index -= 26
       
        return self.alphabet[index]

    def decrypt_or_encrypt_data(self, key_list, mode = 'enc'):
        """Do decryption or Encryption to data, using key list provide outside"""
        dec_data = ''
        for i, enc_char in enumerate(self.enc_data):
            cur_key_letter = key_list[i % len(key_list)]
            dec_char = self.get_new_char(enc_char, cur_key_letter, mode)
            dec_data += dec_char
        return dec_data

if __name__ == '__main__':
    # 5 is key size which get by THE BLACK CHAMBER

    # vc = VigenereCipher(read_file_from('../data_vigenere/vigenere_ct.txt'), 5)
    # vc.exec_analysis('../data_vigenere/')
    # kl = vc.get_keys_from_analysis()
    # decrypt_data = vc.decrypt_or_encrypt_data(kl, 'dec')
    # write_data_to('../data_vigenere/vigenere_pt.txt', decrypt_data)
    # print('decrypt done!')

    # Do encryption to decryption data from chanllenge-2-c2.txt
    kl = ['h', 'a', 'c', 'k', 's']
    vc2 = VigenereCipher(read_file_from('../data/12all-sub.txt'))
    en_data = vc2.decrypt_or_encrypt_data(kl)
    write_data_to('../data_vigenere/c2-vigenere-ct.txt', en_data)
    print('encryption done!')
            