import cv2

# Haar Cascade 파일 불러오기
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# 동영상 파일 불러오기
cap = cv2.VideoCapture('people.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Video file finished or Error.")
        break

    # 그레이스케일 이미지로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 사람 탐지
    bodies = body_cascade.detectMultiScale(gray, 1.1, 4)

    # 사람 별로 사각형 그리기
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, 'Person', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2,
                    lineType=cv2.LINE_AA)

    # 결과 출력
    cv2.imshow('Human Detection', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료
cap.release()
cv2.destroyAllWindows()
