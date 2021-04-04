import os 
import librosa
import random

import soundfile as sf
# import pydub
from os import path
from pydub import AudioSegment

import numpy as np

for subFolder in os.listdir(path.join (path.dirname(path.abspath(__file__)), 'Dataset')):

    #count = 21
    for comm in os.listdir(path.join (path.dirname(path.abspath(__file__)), 'Dataset', str(subFolder))):
        sound = AudioSegment.from_file(path.join(path.dirname(path.abspath(__file__)), 'Dataset', str(subFolder), str(comm)))
        sound_length = len(sound)
        halfway_point = sound_length // 3 
        for i in range(25):
            # print (subFolder, ' ', i)
            start = random.randint(0, halfway_point)
            end = random.randint(0, halfway_point)
            crop_audio = sound[start: sound_length-end]
            # print (start , " ", sound_length-end)
            crop_audio.export('test.wav',format='wav')
            data, sr = librosa.load('test.wav')
            # new_crop = np.pad(data,(0,22026),'constant') # Pad data so that the duration matches (2 Sec)
            #librosa.output.write_wav('./Dataset/'+str(files)+'/'+str(count)+'.wav',new_crop,sf)

            audio_file_path =  path.join (path.dirname(path.abspath(__file__)), 'Dataset', str(subFolder), str(i) + str(comm))

            sf.write(audio_file_path, data, sr, 'PCM_24')   #version - 8
            #count += 1
    #
    print("Done")