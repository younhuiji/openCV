import cv2

# people.mp4 파일을 열어서 VideoCapture 객체를 생성합니다.
cap = cv2.VideoCapture('people.mp4')

# 비디오의 기본 정보를 가져옵니다.
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 기본 정보를 출력합니다.
print(f'Width: {width}')
print(f'Height: {height}')
print(f'Frames Per Second: {fps}')
print(f'Total Frames: {total_frames}')

# 동영상의 총 길이를 계산하고 출력합니다.
total_duration = total_frames / fps
print(f'Total Duration: {total_duration:.2f} seconds')

# VideoCapture 객체를 닫습니다.
cap.release()
