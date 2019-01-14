import scipy.io.wavfile as wavfile
import numpy as np
import copy
from tkinter import filedialog
import os
from sklearn.preprocessing import scale, normalize

def volumeManage(file, volume):

    sampleRate, data = readAudio(file)

    tmp = scale(data)*volume
    #tmp = normalize(data)
    leveling_data = copy.copy(data)

    for i in range(len(data)):
        leveling_data[i] = tmp[i]

    return sampleRate, leveling_data


def readAudio(file):
    #read WAVE file
    wav_sampleRate, wav_data = wavfile.read(file)

    return wav_sampleRate, wav_data