import librosa
import matplotlib.pyplot as plt 
import numpy as np
import librosa.display

data, sr = librosa.load('Dataset/decrease_volume/1.wav')
D = np.abs(librosa.stft(data))
plt.figure(figsize=(20,8))
librosa.display.specshow(librosa.amplitude_to_db(D,ref=np.max),y_axis='log', x_axis='time')
plt.title('Spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.show()