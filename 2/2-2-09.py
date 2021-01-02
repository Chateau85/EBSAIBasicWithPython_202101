import PIL.Image as pilImg
import matplotlib.pyplot as plt
import numpy as np

im1 = pilImg.open('./2-2/baby1.jpg')  # image file 읽어오기

# 이미지 데이터를 numpy array로 구성
pix1 = np.array(im1)
pix1 = (1 / 255) * pix1
pixSize1 = np.array(pix1.shape)

pix2 = np.empty(pixSize1)

for i in range(pixSize1[0]):
    for j in range(pixSize1[1]):
        grayPix = 0.2126 * pix1[i][j][0] + 0.7152 * pix1[i][j][1] + 0.0722 * pix1[i][j][2]  # 회색톤으로 변환
        pix2[i, j] = (grayPix, grayPix, grayPix)  # RGB의 값을 모두 회색톤으로 저장

plt.subplot(141)
plt.imshow(pix1)  # 원본 이미지 출력
plt.axis('off')
plt.title('Original', fontsize=9)

plt.subplot(142)
plt.imshow(pix2)  # 회색톤으로 변환할 이미지 출력
plt.axis('off')
plt.title('Gray converted', fontsize=9)
plt.show()
