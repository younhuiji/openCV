# 2) 그레이 스케일 (흑백처리 )  cv.imread(파일, cv.IMREAD_GRAYSCALE)   /  cv.cvtColor()
import cv2 as cv
im = cv.imread("../img/Lenna.png")
print(type(im))
print(im.shape)  #행, 열, 색상  =  높이 , 폭, 채널
print(im.dtype)

im = cv.imread("../img/Lenna.png",cv.IMREAD_GRAYSCALE )
print(type(im))
print(im.shape)  #행, 열, 색상  =  높이 , 폭, 채널
print(im.dtype)