"""utils"""
import pandas as pd

def read_file_from(path):
    """"read file"""
    f = open(path)
    line = f.readline()
    ret = ""
    while line:
        ret += line
        line = f.readline().strip('\n')
    f.close()

    ret = ret.replace('\n', '')
    return ret

def write_data_to(_path_file, _content):
    """"write file after substituion"""
    _path = '../data/' + _path_file
    with open(_path, 'w') as f:
        f.write(_content)


def write_to_csv(chars, numbers, frequencies, path_file):
    """write in csv"""
    # print(chars, numbers, len(chars), frequencies)
    df = pd.DataFrame({
        'chars': chars,
        'numbers': numbers,
        'frequencies': frequencies
    })
    df.to_csv('../data/' + path_file)
    print('result of analysis has been stored in: ' + path_file)

def statistics_analysis(_dict_chars, _count):
    """input: dict and number of different elements,
    output: statistics_analysis from high frequence to low"""
    sorted_chars = dict(sorted(_dict_chars.items(), key = lambda item:item[1], reverse = True))

    chars = list(sorted_chars.keys())
    numbers =  list(sorted_chars.values())
    frequencies = list(map(lambda x: x/_count, numbers))
    return chars, numbers, frequencies

def arbitary_mapping_sub(org_data, mapping_dict, to_path):
    """ do arbitary mapping substitution by using mapping dict"""
    decrypt_data = ''
    for _ in org_data:
        temp = mapping_dict.get(_)
        decrypt_data += temp
    write_data_to(to_path, decrypt_data)
    print('substitution done! result store in: ' + to_path)
        