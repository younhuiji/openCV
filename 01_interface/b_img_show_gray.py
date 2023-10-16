import cv2  # 설치된 cv2 모듈을 참조하겠다.

img_file = "../img/apple.jpg"
img = cv2.imread(img_file, 0)  #그레이 스케일로 읽기

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    #cv2.destroyAllWindows()
else:
    print('No image file.')
    