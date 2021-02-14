import numpy as np
import math
from cryptanalysis import CryptAnalysis
from utils import *

class TransEncrypt(object):
    """Columnar transposition cipher"""
    def __init__(self, source_data, key):
        self.source_data = source_data
        self.key = key
        self.data_len = len(source_data)
        self.key_digits = int(math.log10(key)) + 1
        self.enc = ''

    def create_array(self):
        """
        create a numpy array
        """
        arr_row = math.ceil(self.data_len / self.key_digits)
        data_arr= np.full((arr_row, self.key_digits), '')
        for i in range(self.data_len):
            data_arr[i // self.key_digits][i % self.key_digits] = self.source_data[i]

        return data_arr

    def key_handle(self, key):
        """
        translate int key to a list
        """
        temp_key_list = []
        while key:
            temp_key_list.append(key % 10)
            key //= 10
        temp_key_list.reverse()
        temp_key_list = list(map(lambda x: x - 1, temp_key_list))
        
        '''
        key replacement
        '''
        l = np.arange(0, len(temp_key_list), 1)
        dict_temp = dict(zip(temp_key_list, l))

        ret = []
        for i in range(0, len(temp_key_list)):
            ret.append(dict_temp[i])

        return ret
    
    def encryption(self, to_path):
        """do encryption write answer to txt file"""
        data_arr = self.create_array()
        # print(data_arr)
        key_list = self.key_handle(self.key)
        # print(key_list)
        
        for i in key_list:
            temp_arr = data_arr[:, i]
            # print(temp_arr)
            self.enc = self.enc + ''.join(temp_arr)
            # print(ret)
            temp_arr = ''

        write_data_to('../data_trans/'+ to_path, self.enc)
        print('transposition encryption done! the result stored in:' + to_path)
    

if __name__ == '__main__':
    data = read_file_from('../data_trans/challenge-2-pt.txt')
    # data = 'attackpostponeduntiltwoamxyz'
    KEY = 23415
    tr = TransEncrypt(data,KEY)
    tr.encryption('c2-trans-ct.txt')
    analy = CryptAnalysis(tr.enc)
    analy.exec(1, '../data_trans/c2-trans-analysis.csv')
    
    
