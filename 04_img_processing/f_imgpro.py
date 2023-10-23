'''
이미지 결합 = 세로 연결 / 가로 연결 / 바둑판 연결
cv.vconcat() - 폭이 동일한 이미지를 세로로 연결
             - 같은 이미지를 반복 세로 연결
             - 폭이 서로 다른 이미지도 세로로 연결
        주의점 : 같은 폭, 같은 채널 수, 데이터 타입 일치, None(오류)

cv.hconcat() - 높이가 동일한 이미지를 가로로 연결
             - 같은 이미지를 반복 가로 연결
            - 높이가 서로 다른 이미지도 가로 연결
        주의점 : 같은 높이, 같은 채널 수, 데이터 타입 일치, None(오류)

np.tile() : 같은 이미지를 반복 정렬
'''
