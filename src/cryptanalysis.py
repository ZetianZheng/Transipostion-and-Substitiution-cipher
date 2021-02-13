""" step 2, get frequency analysis of different chars and write to result1.csv"""
from utils import *


class Crypt1Analysis(object):
    """step 1: analysis """
    def __init__(self, _from_path, _to_path_csv):
        self._from_path = _from_path
        self._to_path_csv = _to_path_csv
        self.exec()
        
    def number_statistics (self, _encrypted_data):
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

    def exec(self):
        """read data from txt, do analysis and rank the chars, write the answer to csv"""
        self.encrypted_data = read_file_from(self._from_path)
        count, dict_chars = self.number_statistics(self.encrypted_data)
        self.chars, numbers, frequencies = statistics_analysis(dict_chars, count)
        write_to_csv(self.chars, numbers, frequencies, self._to_path_csv)

