import numpy as np 
import librosa
import os 
from os import path


peak_features = []
peak_labels = []
count = 0
# val = 0
# val2 = 0

for dirc in sorted(os.listdir(path.join (path.dirname(path.abspath(__file__)), 'Dataset'))):
    for files in os.listdir(path.join(path.dirname(path.abspath(__file__)), 'Dataset',str(dirc))):
        data, sr = librosa.load(path.join(path.dirname(path.abspath(__file__)), 'Dataset',str(dirc),str(files)))
        D = np.abs(librosa.stft(data))

           # print(D.shape)
       
        # val = max(val, D.shape[1])
        # val2 = max(val2, D.shape[0])

# print("maximum value column: " ,val)
# print("maximum value column: ", val2)

        temp = None

        temp = np.zeros((1025, 203))
        temp[: D.shape[0], : D.shape[1]] = D

        # print("Shape after Padding: ", temp.shape)
        peak_features.append(temp)
        peak_labels.append(count)
    
    count += 1  

print("done")

peak_features = np.array(peak_features)
peak_labels = np.array(peak_labels)

print(peak_features.shape)
print(peak_labels.shape)

np.save('./command_spect.npy',peak_features)
np.save('./command_spect_labels.npy',peak_labels)