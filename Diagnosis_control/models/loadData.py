import numpy as np

def formatData(data_tmp):
    
    data = np.zeros(44100)
    data[0:int(data_tmp.size)] = data_tmp[:]
    data = np.reshape(data, (1, 44100, 1))

    return np.array(data)
