import numpy as np                  # 행렬 및 벡터 데이터 관리를 위한 numpy 모듈
import matplotlib.pyplot as plt     # 소리 데이터의 그래프 표현을 위한 모듈
import scipy.io.wavfile as write    # wav 형식으로 소리 데이터를 저장하기 위한 모듈
import os

# sampling rate
Fs = 44100.0            # 정보 샘플링 주파소, 1초에 44100개의 샘플링, 단위는 Hz(주파수)

# 1초 데이터 생성을 위한 환경 변수 설정
tlen = 1                    # 1초로 초기화
Ts = 1 / Fs                 # 샘플링 사이의 간격(시간) 계산
t = np.arange(0, tlen, Ts)  # 소리 데이터를 생성할 시간 성분으로 구성된 배열로 0과 1 사이를 Ts(TimeStamp)의 간격으로 분할하여
                            # Fs 개의 데이터를 담을 수 있는 배열 t를 생성

# 시그널 생성하기
sin_freq = 440                  # 사인 곡선의 주파수
src = 2 * np.pi * sin_freq * t  # t 배열의 각 성분값에 사인함수의 주기를 라디안 단위로 변환한 src 배열을 준비
signal = np.sin(src)            # timestamp를 각으로 변환한 src 배열에 맞게 사인함수 데이터를 변환

# 데이터의 시각화: 생성한 시그널 데이터를 그래프로 표현
x_range = 200                   # 시작부터 200개의 데이터만 보여주기 위한 범위값 지정
plt.plot(t[0:x_range], signal[0:x_range], color='blue')
                                # x축의 timestamp에 사인함수로 생성한 데이터를 y출에 좌표로 그래프를 그림
plt.show()                      # 200개의 데이터를 시각화한 그래프를 보여줌

# 데이터의 시각화: 시그널 데이터를 푸리에 변환하여 주파수 영역에서 시각화함
freq = np.fft.fftfreq(len(t), Ts)   # 주파수 영역에서의 샘플링 구간값의 배열
signal_f = np.fft.fft(signal)       # 사인함수 값으로부터 주파수 영역에서의 정보를 나타내기 위한 푸리에 변환값을 signal_f 배열로 저장
plt.plot(freq[0:x_range], 20*np.log10(np.abs(signal_f[0:x_range])), color='blue')
plt.show()                          # 푸리에 변환된 200개 데이터를 그래프로 출력
