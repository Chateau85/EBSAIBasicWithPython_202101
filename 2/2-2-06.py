# 외부 모듈 정의
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as pilImg

im = pilImg.open('./2-2/rgb_circle.bmp')
pix = np.array(im)
pixSize = np.array(pix.shape)
print(pixSize)
# pix array에서 각각 R(0), G(1), B(2) 성분값 외에는 0으로 만든 후
# 원본 이미지에서 R, G, B에 해당하는 배열 만들기
pix_R = pix.copy()
pix_R[:, :, (1, 2)] = 0
pix_G = pix.copy()
pix_G[:, :, (0, 2)] = 0
pix_B = pix.copy()
pix_B[:, :, (0, 1)] = 0

# 원본 이미지인 pix 행렬을 이미지 데이터로 출력
plt.subplot(141)
plt.imshow(pix)
plt.axis('off')
plt.title('RGB')

# pix 행렬에서 이미지 데이터의 R 채널 출력
plt.subplot(142)
plt.imshow(pix_R)
plt.axis('off')
plt.title('R(Red)')

# pix 행렬에서 이미지 데이터의 G 채널 출력
plt.subplot(143)
plt.imshow(pix_G)
plt.axis('off')
plt.title('G(Green)')

# pix 행렬에서 이미지 데이터의 B 채널 출력
plt.subplot(144)
plt.imshow(pix_B)
plt.axis('off')
plt.title('B(Blue)')
plt.show()