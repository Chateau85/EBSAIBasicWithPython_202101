import numpy as np
import scipy.io as sio
from scipy.io.wavfile import write
import os
import matplotlib.pyplot as plt     # 소리 데이터의 그래프 표현을 위한 모듈
v_samplerate, v_data = sio.wavfile.read('2-3/thank_you.wav')
b_samplerate, b_data = sio.wavfile.read('2-3/Invisible_Beauty.wav')

v_times = np.arange(len(v_data)) / float(v_samplerate)
b_times = np.arange(len(b_data)) / float(b_samplerate)

plt.plot(v_times, v_data)
plt.xlim(v_times[0], v_times[-1])
plt.xlabel('voice time (s)')
plt.ylabel('amplitude')
plt.show()
plt.plot(b_times, b_data)
plt.xlabel('bg time (s)')
plt.ylabel('amplitude')
plt.show()