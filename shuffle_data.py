from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

x_data = np.load("E://SPL3//SPL3//MainCode//SpeechRecognition//command_spect.npy")
y_data = np.load("E://SPL3//SPL3//MainCode//SpeechRecognition//command_spect_labels.npy")

enc = OneHotEncoder()
y_data = enc.fit_transform(y_data.reshape(-1, 1)).toarray()
print(y_data)
# y_data = np.array(y_data)
x_data, y_data = shuffle(x_data, y_data)
X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2,stratify=y_data,random_state=42)

X_train = X_train.reshape((-1,1025,203,1))
X_test = X_test.reshape((-1,1025,203,1))

np.save("E://SPL3//SPL3//MainCode//SpeechRecognition//speech_recognition_tools//X_train.npy", X_train)
np.save("E://SPL3//SPL3//MainCode//SpeechRecognition//speech_recognition_tools//X_test.npy", X_test)
np.save("E://SPL3//SPL3//MainCode//SpeechRecognition//speech_recognition_tools//y_train.npy", y_train)
np.save("E://SPL3//SPL3//MainCode//SpeechRecognition//speech_recognition_tools//y_test.npy", y_test)
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)