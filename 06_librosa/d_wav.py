import numpy as np
import soundfile as sf
import h5py


# Numpy 배열 파일 읽는 함수
def read_npy(filename):
    return np.load(filename)


# 오디오 파일 읽는 함수
def read_audio(filename):
    y, sr = sf.read(filename)
    return y, sr


# 텍스트 파일 읽는 함수
def read_txt(filename):
    return np.loadtxt(filename)


# HDF5 파일 읽는 함수
def read_hdf5(filename):
    with h5py.File(filename, 'r') as hf:
        harmonic = np.array(hf['harmonic'][:])
        percussive = np.array(hf['percussive'][:])
    return harmonic, percussive



if __name__ == "__main__":
    # Numpy 파일 읽기
    y_harmonic_npy = read_npy('harmonic.npy')
    y_percussive_npy = read_npy('percussive.npy')
    print(f"Read from npy - Harmonic: {y_harmonic_npy[:10]}, Percussive: {y_percussive_npy[:10]}")

    # 오디오 파일 읽기
    y_harmonic_audio, sr_harmonic = read_audio('harmonic.wav')
    y_percussive_audio, sr_percussive = read_audio('percussive.wav')
    print(f"Read from audio - Harmonic: {y_harmonic_audio[:10]}, Percussive: {y_percussive_audio[:10]}")

    # 텍스트 파일 읽기
    y_harmonic_txt = read_txt('harmonic.txt')
    y_percussive_txt = read_txt('percussive.txt')
    print(f"Read from txt - Harmonic: {y_harmonic_txt[:10]}, Percussive: {y_percussive_txt[:10]}")

    # HDF5 파일 읽기
    y_harmonic_hdf5, y_percussive_hdf5 = read_hdf5('harmonic_percussive.h5')
    print(f"Read from hdf5 - Harmonic: {y_harmonic_hdf5[:10]}, Percussive: {y_percussive_hdf5[:10]}")
