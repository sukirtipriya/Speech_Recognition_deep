# Audio file formats
# .mp3
# .flac
# .wav

import wave

# Audio signal parameters
# - number of channels
# - sample width
# - framerate/sample_rate: 44,100Hz
# - number of frames
# - values of a frame

obj = wave.open("audiofile.wav","rb")

print("Number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)

obj.close()

obj_new = wave.open("audiofile_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()

## Plot audio ########################################################################

# pip install matplotlib numpy

import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("audio.wav", "rb")


sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples / sample_freq

print(t_audio)


signal_array = np.frombuffer(signal_wave, dtype = np.int16)

times = np.linspace(0, t_audio, num = n_samples)

plt.figure(figsize =(15,5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()

## Record audio #################################################################

import pyaudio
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.pyAudio()

stream = p.open(
     format = FORMAT,
     channels = CHANNELS,
     rate = RATE,
     input = True,
     frames_per_buffer = FRAMES_PER_BUFFER
)
   
print("start recording")

seconds = 5
frames = []

for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
     data = stream.read(FRAMES_PER_BUFFER)
     frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav", "wb")
obj.sentnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()

## load mp3 ###########################################################################

from pydub import AudioSegment

audio = AudioSegment.from_wav("audiofile.wav")

# incrase the volume by 6db

audio = audio + 6
audio = audio* 2
audio = audio.fade_in(2000)
audio.export("mashup.mp3", format = "mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")




