import cv2
import numpy as np
from matplotlib import pyplot as plt
# 히스토그램을 계산하여 "sample_puppy.jpg"와 가장 유사한 영역을 "puppy.jpg"에서 찾아
# 해당 영역에 사각형을 그려 시각화하자.
# 두개의 이미지 -> 히스토그램 -> 정규화 -> 유사도 -> 박스
def find_puppy_using_histogram(img_path, templ_path):
    img = cv2.imread(img_path)
    templ = cv2.imread(templ_path)

    # 이미지와 템플릿의 히스토그램을 계산합니다.
    img_hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    templ_hist = cv2.calcHist([templ], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

    # 히스토그램을 정규화합니다. -> 두개의 이미지 비교 후 유사도 확인
    cv2.normalize(img_hist, img_hist)
    cv2.normalize(templ_hist, templ_hist)

    # 히스토그램 비교
    img_height, img_width = img.shape[:2]   # 입력 이미지의 높이, 너비
    templ_height, templ_width = templ.shape[:2] # 템플릿 이미지 높이, 너비
    result_width = img_width - templ_width + 1

    # 두개의 높이와 너비를 계산한다.
    result_height = img_height - templ_height + 1
    result = np.zeros((result_height, result_width), dtype=np.float32)

    # 히스토그램을 사용해서 템플릿을 매칭하는 부분
    for i in range(result_height):
        for j in range(result_width):
            sub_img = img[i:i+templ_height, j:j+templ_width] # 입력 이미지에서 부분 이미지 추출

            sub_img_hist = cv2.calcHist([sub_img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
            cv2.normalize(sub_img_hist, sub_img_hist)

            # 템플릿의 히스토그램과 부분이미지의 히스토그램을 비교해서 유사도를 비교
            d = cv2.compareHist(templ_hist, sub_img_hist, cv2.HISTCMP_CORREL)
            result[i, j] = d

    # max_val, max_loc 는 가장 높은 상관관계를 가지는 부분과 위치 값을 가진다.
    # 템플릿이 입력 이미지에 어디에 위치하는지 알 수 있다.
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 가장 유사한 위치에 사각형을 그립니다.
    top_left = max_loc
    bottom_right = (top_left[0] + templ_width, top_left[1] + templ_height)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Matching Result')
    plt.show()

if __name__ == '__main__':
    find_puppy_using_histogram('puppy.jpg', 'sample_puppy.jpg')
