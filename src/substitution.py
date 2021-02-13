from utils import *

class Substituion(object):
    """substitution with guessing and analysis"""
    def __init__(self, _org_data, _mapping_dict, _to_path):
        self._org_data = _org_data
        self._mapping_dict = _mapping_dict
        self._to_path = _to_path
        self.arbitary_mapping_sub()

    def arbitary_mapping_sub(self):
        """ do arbitary mapping substitution by using mapping dict"""
        decrypt_data = ''
        for _ in self._org_data:
            temp = self._mapping_dict.get(_)
            decrypt_data += temp
        write_data_to(self._to_path, decrypt_data)
        print('substitution done! result store in: ' + self._to_path)
        