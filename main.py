import numpy as np

def read_file(file_name):
    data = np.genfromtxt(file_name, delimiter=',')
    return data

