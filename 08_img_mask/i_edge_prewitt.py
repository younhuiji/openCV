import cv2
import numpy as np

file_name = "e.jpg"
img = cv2.imread(file_name)

# 프리윗 커널 생성
gx_k = np.array([[-1,0,1], [-1,0,1],[-1,0,1]]) # 수평 방향의 변화를 측정하는 커널
gy_k = np.array([[-1,-1,-1],[0,0,0], [1,1,1]]) # 수직 방향의 변화를 측정하는 커널

# 프리윗 커널 필터 적용
edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

# 결과 출력
merged = np.hstack((img, edge_gx, edge_gy, edge_gx+edge_gy))
cv2.imshow('prewitt', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()