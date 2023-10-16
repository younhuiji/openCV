import cv2 as cv    # - as 별칭 : cv2모듈을 cv라는 별칭으로 사용하겠다.

img_file = "../img/apple.jpg" # 표시할 이미지 경로            ---①
img = cv.imread(img_file)  # 이미지를 읽어서 img 변수에 할당 ---②

if img is not None:
  cv.imshow('MyIMG', img)   # 읽은 이미지를 화면에 표시      --- ③
  cv.waitKey()           # 키가 입력될 때 까지 대기      --- ④
  cv.destroyAllWindows()  # 창 모두 닫기            --- ⑤
else:
    print('No image file.')
    