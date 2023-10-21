# 오디오 파일 "작은별.mp3"을 로드하여 하모닉과 타악기 성분을 추출해서 저장해 보자.
import librosa
import numpy as np
import soundfile as sf
import h5py


# 오디오 파일 로드 함수
def load_audio(filename):
    y, sr = librosa.load(filename)
    return y, sr


# Numpy 배열을 파일로 저장하는 함수
def save_as_npy(array, filename):
    np.save(filename, array)


# 오디오 파일로 저장하는 함수
def save_as_audio(array, filename, sr=44100):
    sf.write(filename, array, sr)


# 텍스트 파일로 저장하는 함수
def save_as_txt(array, filename):
    np.savetxt(filename, array)


# HDF5 = Hierarchical Data Format version 5 파일로 저장하는 함수
def save_as_hdf5(array1, array2, filename):
    with h5py.File(filename, 'w') as hf:
        hf.create_dataset('harmonic', data=array1)
        hf.create_dataset('percussive', data=array2)


# main 코드
if __name__ == "__main__":
    # 오디오 로드
    y, sr = load_audio("작은별.mp3")

    # 하모닉과 타악기 성분 추출
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    # 저장 예시 / 배열 numpy 저장
    save_as_npy(y_harmonic, 'harmonic.npy')
    save_as_npy(y_percussive, 'percussive.npy')

    # wav 음악파일로 저장
    save_as_audio(y_harmonic, 'harmonic.wav', sr)
    save_as_audio(y_percussive, 'percussive.wav', sr)

    # 메타데이터로 변환할 수 있는 저장 파일 (.json( mongodb server/bson -> .json), / .xml, .csv(tsv) )
    save_as_txt(y_harmonic, 'harmonic.txt')
    save_as_txt(y_percussive, 'percussive.txt')

    save_as_hdf5(y_harmonic, y_percussive, 'harmonic_percussive.h5')
