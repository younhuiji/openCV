# 이미지 파일을 읽고 , 저장   imread(), imwrite(파일이름 , 대상,,,) , imshow()
import numpy as np
import  cv2  as cv

im = cv.imread("../img/Lenna.png")
print(type(im))
print(im.shape)  #행, 열, 색상  =  높이 , 폭, 채널
print(im.dtype)

#색상의 순서   BGR
#im[:,:,(0,1)] =  0   #0번째 (B:파랑)과  1번째  (G:녹색)을   0 (검정)으로 지정
cv.imshow("my view",im)
#출력
cv.imwrite("../img_res/Lena_b01.png",im,[cv.IMWRITE_JPEG_QUALITY, 9])  #cv.imwrite(파일이름, 대상 )

cv.imwrite("../img_res/Lena_b02.jpg",im, [cv.IMWRITE_JPEG_QUALITY, 50] )  #cv.imwrite(파일이름, 대상, )
cv.imwrite("../img_res/Lena_b03.jpg",im, params=[cv.IMWRITE_JPEG_QUALITY, 1])  #cv.imwrite(파일이름, 대상, )
cv.imwrite("../img_res/Lena_b04.jpg",im) #95

#원본을 로드(png,bmp)  -> 저장  -> jpg로드시 화소가 달라진다.

# jpg (1~ 95)  기본값은 75   / jpg  0 ~100  기본값은 95
#png   0~9  기본값은  3
# 확장자의 압축률이 높을 수록  로딩 하는  속도가 느려진다.
