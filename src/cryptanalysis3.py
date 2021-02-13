from utils import *

class Crypt3Analysis(object):
    """step 3: analysis triple chars frequency and write to  result3.csv"""
    def __init__(self, _from_path, _to_path_csv):
        self._from_path = _from_path
        self._to_path_csv = _to_path_csv
        self.exec()

    def number_3_statistics(self, _encrypted_data):
        """ return a number of all different 2 length words
        the dict of that and numbers of a pair chars"""
        dict_char = {}
        count = 0
        temp_list = []
        for i in range(0, len(_encrypted_data) - 2):
            temp_list.append(_encrypted_data[i])
            temp_list.append(_encrypted_data[i + 1])
            temp_list.append(_encrypted_data[i + 2])
            temp_str = "".join(temp_list)
            if temp_str in dict_char:
                dict_char[temp_str] += 1
            else:
                dict_char[temp_str] = 1
            temp_list = []
            count += 1
        return count, dict_char


    def exec(self):
        """ execution function"""
        self.encrypted_data = read_file_from(self._from_path)
        count, dict_chars = self.number_3_statistics(self.encrypted_data)
        self.chars, numbers, frequencies = statistics_analysis(dict_chars, count)
        write_to_csv(self.chars, numbers, frequencies, self._to_path_csv)
