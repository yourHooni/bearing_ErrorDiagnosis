import os
import numpy as np

from preprocessing import BandpassFiltering
from preprocessing import volumeManage_range
from preprocessing import fft_
from preprocessing import original_
import predict

tire_weightpath = 'D:/tire_weights.h5'

# get soundfile(.wav)
def getSoundfile():
    file_dir = "C:/Users/User/Desktop/test023_mono.wav"

    return file_dir

def do_bandpass(file_dir):
    tire_wavefile = BandpassFiltering.bandpass_filter(file_dir, 20, 100, "C:/Users/User/Desktop/test023_mono_tire.wav")
    bearing_wavefile = BandpassFiltering.bandpass_filter(file_dir, 500, 600, "C:/Users/User/Desktop/test023_mono_bearing.wav")

    return tire_wavefile, bearing_wavefile

def do_normalize(file_dir):
    volume = 3000

    sampleRate, data = volumeManage_range.volumeManage(file_dir, 3000)

    return sampleRate, data

def do_fft(sampleRate, data):
    fft_data = fft_.fft(sampleRate, data)
    np.save('C:/Users/User/Desktop/test023_mono_bearing.npy', data)

    return fft_data

def do_original(sampleRate, data):
    original_data = original_.original_audio(sampleRate, data)
    np.save('C:/Users/User/Desktop/test023_mono_tire.npy', data)

    return original_data

def do_predict(pred_data, weightpath):
    result = predict.predict(pred_data, weightpath)

    return result

def main():
     sound_dir = getSoundfile()
     tire_wavefile, bearing_wavefile = do_bandpass(sound_dir)

     tire_sampleRate, tire_data = do_normalize(tire_wavefile)
     bearing_sampleRate, bearing_data = do_normalize(bearing_wavefile)

     tire_character_data = do_fft(tire_sampleRate, tire_data)
     #tire_character_data = do_original(tire_sampleRate, tire_data)
     #bearing_character_data = do_fft(bearing_sampleRate, bearing_data)

     tire_result = do_predict(tire_character_data, tire_weightpath)
     #bearing_result = do_predict(bearing_character_data)

     return tire_result
     #return tire_result, bearing_result



