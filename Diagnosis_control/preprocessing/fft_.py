import scipy.io.wavfile as wavfile
import numpy as np
import librosa
import librosa as fft
import matplotlib.pyplot as plt
import os

def fft(sampleRate, data):
    # Discrete time signal
    amplitude = data #signal amplitude vector
    fs = sampleRate
    N = data.size #number of samples in wav_data
    t = np.arange(N) /fs
    
    # FFT
    NFFT = 512
    dft_data = np.fft.fft(data)/NFFT #DFT vector (Complex Numbers)
    dft_phase = np.angle(dft_data) #DFT phase (Angle in rads)
    dft_amplitude = np.abs(dft_data) #DFT Amplitude (Magnitude)
    dB = 20 * np.log10(dft_amplitude / np.max(dft_amplitude))
    dt = 1/float(fs) #sample spacing(inverse of sample rate)
    dft_freq = np.fft.fftfreq(N,dt) #DFT sample frequency vector
   

    #미분
    derivative_amplitude_data ,derivative2_amplitude_data = derivativeData(dft_amplitude)

    # fft feature
    fft_feature = (dft_amplitude - np.mean(dft_amplitude)) / np.std(dft_amplitude) #정규화

    derivative_fft_feature ,derivative2_fft_feature = derivativeData(fft_feature)

    return derivative_amplitude_data


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