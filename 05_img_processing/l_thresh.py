'''

cv2에서 문서, 이미지 처리 또는 투영변화가 되는 함수
    1. cvtColor() : 색공간 변화 함수
    2. GaussinanBlur() : 가우시안블러를 사용해서 노이즈(잡음)를 줄인다.

    3. threshold() : 임계값을 사용한 대비    ->  노이즈가 적고, 객체와 명암 차이가 뚜렷할 때 사용한다.
                                        ->  객체 겹침이 적고 개수가 많지 않을 경우 사용한다.

    4. findCountours() : 윤곽선을 찾아서 명함 또는 문서(대상)의 테두리를 감지한다.
    5. warpPerspective(), getPerspectiveTransform() : 사각형 테두리 보정할 때 사용
    6. createCLAHE() : 히스토그램이미지(equalizeHist()) 대비개선을 구현했을 때를 다시 대비
    7. drawCountours() : 윤곽선을 그릴 때 사용

========================================================================

         감마 보정                      임계값 처리의 차이

목적      전체 이미지 밝기                 이진화 -> 객체 배경 분리
작동방식   픽셀지수연산=이미지 대비보정        임계값을 기준으로 픽셀값을 0 또는 255로 설정
적용      사진의 색깔을 자연스럽게           객체검출, 텍스트 추출, 윤곽선 찾기
         (디스플레이간의 색차이를 줄일때 사용)

========================================================================

임계값 처리 : 이미지 처리중에 가장 많이 사용하는 처리방식 0~ 255 중에서 127의 값을
            깃점으로 127보다 작은 모두 0, 127보다 크면 255로 처리를 하게 된다.
이미지를 2진화 분류하는 작업 : 흰색과 검정으로 분류

cv.threshold( 대상이미지, 임계값, 임계값 보다 큰값,  적용타입)
cv.threshold( src, thresh,    maxval,  type)

type의 속성값들
cv.THRESH_BINARY  : 픽셀값   IMG(X,Y)  thresh 값보다 크면  value,  작으면   0
cv.THRESH_BINARY_INV: 픽셀값   IMG(X,Y)  thresh 값보다 크면  0,  작으면   value
cv.THRESH_TRUNC :  픽셀값   IMG(X,Y)  thresh 값보다 크면  thresh,  작으면   픽셀값IMG(X,Y)
cv.THRESH_TOZERO : 픽셀값   IMG(X,Y)  thresh 값보다 크면  픽셀값 IMG(X,Y)  , 작으면 0으로 채움
cv.THRESH_TOZERO_INV :  픽셀값   IMG(X,Y)  thresh 값보다 크면 0  , 작으면  픽셀값 IMG(X,Y)
'''
# << 임계값 지정해서   이미지를  확인 해보자>>
import cv2 as cv
import matplotlib.pyplot as plt

# 이미지를 불러온다.
image = cv.imread('../img/Lenna.png')

# 이미지를 그레이스케일로 변환한다.
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# 임계값을 적용한다. 여기서는 128을 기준으로 임계값을 적용하였다.
# 128 이하의 값은 0으로, 128 초과의 값은 255로 설정한다.
ret, thresh1 = cv.threshold(gray_image, 128, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(gray_image, 128, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(gray_image, 128, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(gray_image, 128, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(gray_image, 128, 255, cv.THRESH_TOZERO_INV)

# 결과를 Matplotlib를 사용하여 출력한다.
titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [gray_image, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
