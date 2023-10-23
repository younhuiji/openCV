import cv2
import numpy as np

# BFMatcher : 특징이 얼마나 유사한지를 확인

# 이미지를 읽어온다.
img1 = cv2.imread('apple.jpg', cv2.IMREAD_GRAYSCALE)  # 원본 이미지
img2 = cv2.imread('apples.jpg', cv2.IMREAD_GRAYSCALE)  # 비교 대상 이미지

# ORB 디텍터를 생성한다.
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# BFMatcher 객체를 생성하고, 키포인트 간의 거리를 측정한다.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# 디스크립터 간의 매칭을 수행한다.
matches = bf.match(des1, des2)

# 매칭 결과를 거리에 따라 정렬한다.
matches = sorted(matches, key = lambda x:x.distance)

# 매칭 결과를 그린다.
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# 결과를 출력한다.
cv2.imshow('Feature Matching', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
