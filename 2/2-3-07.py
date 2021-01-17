import numpy as np
import scipy.io as sio
from scipy.io.wavfile import write
import os
v_samplerate, v_data = sio.wavfile.read('2-3/thank_you.wav')
b_samplerate, b_data = sio.wavfile.read('2-3/Invisible_Beauty.wav')

v_times = np.arange(len(v_data)) / float(v_samplerate)
b_times = np.arange(len(b_data)) / float(b_samplerate)

print('sampling rate: ', v_samplerate, b_samplerate)
print('time: ', v_times[-1], b_times[-1])
print('len: ', len(v_data), len(b_data))

print(v_data.shape)
print(b_data.shape)
