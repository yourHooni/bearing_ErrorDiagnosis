import librosa
import os
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import math
import numpy as np

k = 1

def original_audio(wav_sampleRate, wav_data):
    
    # Discrete time signal
    amplitude = wav_data #signal amplitude vector
    fs = wav_sampleRate
    N = wav_data.size #number of samples in wav_data
    t = np.arange(N) /fs
   
    derivative_wav_data ,derivative2_wav_data = derivativeData(wav_data)

    period_data = period(amplitude)
    
    derivative_period_data ,derivative2_period_data = derivativeData(period_data)

    return derivative_wav_data

def period(amplitude):
    # 주기
    period_data = []
    prev_index = 0

    for i in range(1, len(amplitude)):
        if compareReverse(amplitude[i-1], amplitude[i]) == 1:
            #print(i)
            if len(period_data) == 0:
                period_data.append(i)
            else:
                period_data.append(i - prev_index)
            prev_index = i
    
    # Original
    #n_groups = len(period_data)
    #index = np.arange(n_groups)

    return period_data

def compareReverse(a, b):
    global k
    #print(a, end=' ')
    #print(b)
    if k>0:
        if a>b:
            k = k * (-1)
            return 1
        else: 
            return 0
    elif k<0:
        if a<b:
            k = k * (-1)
            return 1
        else:
            return 0
            
def name():
    dnxkj

# 미분
def derivativeData(data):
    derivative_data = []
    temp_data = np.append(data, data[0])
    for i in range(len(temp_data) - 1):
        derivative_data.append(temp_data[i + 1] - temp_data[i])
    derivative_data = np.array(derivative_data)

    derivative2_data = []
    temp_data = np.append(derivative_data, derivative_data[0])
    for i in range(len(temp_data) - 1):
        derivative2_data.append(temp_data[i + 1] - temp_data[i])
    derivative2_data = np.array(derivative2_data)

    return derivative_data, derivative2_data
