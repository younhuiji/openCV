from moviepy.editor import VideoFileClip
import cv2
import numpy as np
import wave
import pandas as pd


# 소리 추출
def extract_audio(video_filename, audio_filename):
    clip = VideoFileClip(video_filename)
    clip.audio.write_audiofile(audio_filename)

    with wave.open(audio_filename, 'r') as wav_file:
        framerate = wav_file.getframerate()
        nframes = wav_file.getnframes()
        duration = nframes / float(framerate)

    audio_features = {
        "framerate": framerate,
        "nframes": nframes,
        "duration": duration
    }

    audio_df = pd.DataFrame([audio_features])
    audio_df.to_csv('audio_features.csv', index=False)


# 해리스 코너 추출
def extract_harris_corners(video_filename):
    cap = cv2.VideoCapture(video_filename)

    harris_data = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)

        dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        corners = np.argwhere(dst > 0.01 * dst.max())

        for corner in corners:
            y, x = corner
            harris_data.append({"x": x, "y": y})

    harris_df = pd.DataFrame(harris_data)
    harris_df.to_csv('harris_corners.csv', index=False)

    cap.release()
    cv2.destroyAllWindows()


# 소리를 'audio_only.wav'로 추출
extract_audio('people_dancing.mp4', 'audio_only.wav')

# 해리스 코너를 추출하여 CSV 파일로 저장
extract_harris_corners('people_dancing.mp4')
