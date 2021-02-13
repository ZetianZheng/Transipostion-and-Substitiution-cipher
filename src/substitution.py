from utils import *

class Substituion(object):
    """substitution with guessing and analysis"""
    def __init__(self, org_data, mapping_dict):
        self._org_data = org_data
        self._mapping_dict = mapping_dict

   