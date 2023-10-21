# Beat tracking example
import librosa

# 1. Get the file path to an included audio example
filename = librosa.example('nutcracker')

##### 데이터 재해석 -> 머신러닝, 딥러닝 (70% = 학습, 30% = 테스트 검증)
# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename) # 원본 원시 오디오 데이터, 샘플링 속도 = 데이터 재해석
print(f"{sr}Hz") #22050Hz -> 디지털 오디오를 표현하기 위해 연속적인 아날로그 신호를 얼마나 자주 샘플링(표본화) 하는 지 표현하는 수치

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print('---------------------------')
print(beat_times)
