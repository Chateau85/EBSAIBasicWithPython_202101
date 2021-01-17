import numpy as np
import scipy.io as sio
from scipy.io.wavfile import write
import os
v_samplerate, v_data = sio.wavfile.read('2-3/thank_you.wav')
b_samplerate, b_data = sio.wavfile.read('2-3/Invisible_Beauty.wav')

v_times = np.arange(len(v_data)) / float(v_samplerate)
b_times = np.arange(len(b_data)) / float(b_samplerate)

# stereo channel을 mono channel로 변경
if len(v_data.shape) > 1 :
    v_data = np.array(v_data[:, 0])
if len(b_data.shape) > 1 :
    b_data = np.array(b_data[:, 0])

# downsampling: 2개의 소리 데이터 샘플링 주파수 중 더 낮은 샘플링 주파수 값으로 변경
if v_samplerate > b_samplerate :
    diffRate = int(v_samplerate / b_samplerate)
    v_data = np.array(v_data[0:len(v_data):diffRate])
    sr = b_samplerate
elif v_samplerate < b_samplerate :
    diffRate = int(b_samplerate / v_samplerate)
    b_data = np.array(b_data[0:len(b_data):diffRate])
    sr = v_samplerate
else:
    sr = b_samplerate

# 10초 지점의 배경 음악과 음성 데이터 합성하기
mix_data = v_data + b_data[sr*10:len(v_data)+sr*10]

# 배경 음악 10초 위치에 합성한 데이터를 넣기
b_data[sr*10:len(v_data)+sr*10] = mix_data

# 합성한 데이터를 wav 파일로 저장하기
scaled = np.int16(b_data/np.max(np.abs(b_data)) * 32767)
write('music_card.wav', sr, scaled)
os.system('start music_card.wav')
