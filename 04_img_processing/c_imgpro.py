import cv2 as cv
im = cv.imread("../img/Lenna.png")
print(type(im))
print(im.shape)  #행, 열, 색상  =  높이 , 폭, 채널
print(im.dtype)

im02 = cv.cvtColor(im, cv.COLOR_BGR2GRAY)  # 회색조로 읽어 온다.
print(type(im02))
print(im02.shape)  #행, 열, 색상  =  높이 , 폭, 채널
print(im02.dtype)

print(im02)
#저장
cv.imwrite('../img_res/Lenna_G.jpg', im02)