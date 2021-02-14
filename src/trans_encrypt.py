import numpy as np
import math

class TransEncrypt(object):
    def __init__(self, source_data, key):
        self.source_data = source_data
        self.key = key
        self.data_len = len(source_data)
        self.key_digits = int(math.log10(key)) + 1
    
    def create_array(self):
        """
        create a numpy array
        """
        arr_row = math.ceil(self.data_len / self.key_digits)
        data_arr= np.full((arr_row, self.key_digits), '')
        for i in range(self.data_len):
            data_arr[self.data_len // self.key_digits][self.data_len % self.key_digits] = self.source_data[i]
        
        return data_arr
    
    def key_handle(self, key):
        """
        translate int key to a list
        """
        key_digits = int(math.log10(key)) + 1
        key_array = [0] * key_digits
        for i in range(key_digits):
            div = key_digits - i - 1 # Dividend
            key_array[i] = int(key // math.pow(10, div))
        return key_array

    
    def encryption(self):
        pass
        