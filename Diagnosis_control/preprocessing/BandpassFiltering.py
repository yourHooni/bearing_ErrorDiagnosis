from pylab import *
import numpy as np
import wave
import sys
import math
import contextlib
from scipy.signal import *
import os

def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

    if sample_width == 1:
        dtype = np.uint8 # unsigned char
    elif sample_width == 2:
        dtype = np.int16 # signed 2-byte short
    else:
        raise ValueError

    channels = np.fromstring(raw_bytes, dtype=dtype)

    if interleaved:
        channels.shape = (n_frames, n_channels)
        channels = channels.T
    else:
        channels.shape = (n_channels, n_frames)

    return channels 

#입력 파일 속성 가져 오기
#with contextlib.closing(wave.open(fname,'rb')) as spf:
def bandpass_filter(file, freqLow, freqHi, out_directory):

    spf = wave.open(file,'rb')

    sampleRate = spf.getframerate()
    sampWidth = spf.getsampwidth()
    nChannels = spf.getnchannels()
    nFrames = spf.getnframes()

    #주파수 입력을위한 디스플레이 명령
    freqHi = freqHi/((sampleRate)/2)
    freqLow = freqLow/((sampleRate)/2)
    
    #wav 파일에서 오디오 추출
    signal = spf.readframes(nFrames*nChannels)
    spf.close()
    channels = interpret_wav(signal, nFrames, nChannels, sampWidth, True)
    
    
    #필터에 사용 된 주파수는 정규화 된 주파수
    bpf = firwin(1001, cutoff=[freqLow, freqHi], window='blackmanharris',pass_zero=False) 
    #channels[0] = channels[0]*0.8   
    filtered = lfilter(bpf,[1], channels[0]).astype(channels.dtype)
   
    wav_file = wave.open(out_directory, "w")
    wav_file.setparams((1, sampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
    wav_file.writeframes(filtered.tobytes('C'))
    wav_file.close()

    return out_directory

