import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
'''
 (1) "작은별.mp3" 파일을 로드
 (2) 웨이브폼을 표시
 (3) 스펙트로그램을 생성
 (4) 비트를 추적

'''
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def load_audio(filename):
    return librosa.load(filename)

def display_waveform(y, sr):
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title('Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

def display_spectrogram(y, sr):
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    plt.title('Spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.show()

def track_beats(y, sr):
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    print(f"Estimated tempo: {tempo} BPM")
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    print(f"Beat times in seconds: {beat_times}")



if __name__ == '__main__':
        # 오디오 파일 로드   https://gongu.copyright.or.kr/gongu/wrt/wrt/view.do?wrtSn=9021707&menuNo=200020
        y, sr = load_audio("작은별.mp3")

        # 웨이브폼 표시
        display_waveform(y, sr)

        # 스펙트로그램 생성
        display_spectrogram(y, sr)

        # 비트 추적
        track_beats(y, sr)
