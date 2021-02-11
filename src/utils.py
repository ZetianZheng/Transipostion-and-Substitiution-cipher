"""utils"""
import pandas as pd

ANSPATH = '../data/results.csv'

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

def write_data_to(path, content):
    with open(path, 'w') as f:
        f.write(content)


def write_to_csv(chars, numbers, frequencies):
    """write in csv"""
    # print(chars, numbers, len(chars), frequencies)
    df = pd.DataFrame({
        'chars': chars,
        'numbers': numbers,
        'frequencies': frequencies
    })
    df.to_csv(ANSPATH)