import cv2

# 비디오를 읽어옵니다.
cap = cv2.VideoCapture("people_dancing.mp4")

# 비디오 저장을 위한 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('people_dancing_labeled.mp4', fourcc, 30.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # 라벨을 추가합니다. 여기서는 왼쪽 상단에 'Dancing'이라는 라벨을 추가합니다.
        cv2.putText(frame, 'Dancing', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # 라벨이 추가된 프레임을 저장합니다.
        out.write(frame)

        # 라벨이 추가된 프레임을 화면에 보여줍니다.
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 자원을 해제합니다.
cap.release()
out.release()
cv2.destroyAllWindows()
