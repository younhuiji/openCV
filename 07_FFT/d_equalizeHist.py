import cv2
def equalize_color_image(image_path, output_path):
    # 이미지 읽기
    img = cv2.imread(image_path)

    # 이미지를 YCrCb 컬러 공간으로 변환 = Y채널에 적용 / HSV = V채널에 적용
    img_y_cr_cb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # Y(밝기), Cr(Y와 결합컬러), Cb 채널 분리
    y, cr, cb = cv2.split(img_y_cr_cb)

    # Y 채널에 대해서만 히스토그램 평활화 적용
    y_eq = cv2.equalizeHist(y)

    # 평활화된 Y 채널과 원래의 Cr, Cb 채널을 다시 합치기
    img_y_cr_cb_eq = cv2.merge([y_eq, cr, cb])

    # YCrCb 컬러 공간을 다시 BGR 컬러 공간으로 변환
    img_bgr_eq = cv2.cvtColor(img_y_cr_cb_eq, cv2.COLOR_YCrCb2BGR)

    # 결과 이미지 저장
    cv2.imwrite(output_path, img_bgr_eq)

# 함수 호출
equalize_color_image('trail.jpg', 'trail_res02.jpg')
