from PIL import Image,ImageFilter,ImageOps
import numpy as np
import matplotlib.pyplot as plt

image=Image.open('images.jpeg')
image.show()

out1=image.resize((200,200))
out1.save("resize.jpg")

out2=ImageOps.grayscale(image)
out2.save("grayscale.jpg")

out3=out2.filter(ImageFilter.GaussianBlur(radius=2))
out3.save('GaussianBlur.jpg')

out4=image.filter(ImageFilter.FIND_EDGES)
out4.save("EdgeDetection.jpg")

image=image.convert('RGB')
red,green,blue=image.split()
def calculate_histogram(channel):
    histogram, bin_edges = np.histogram(np.array(channel).flatten(), bins=256, range=(0, 255))
    return histogram

# Calculate histograms for each channel
red_hist = calculate_histogram(red)
green_hist = calculate_histogram(green)
blue_hist = calculate_histogram(blue)

# Plotting the histograms in a single graph
plt.title("Colour Histogram")
plt.xlabel("bins")
plt.ylabel("# of Pixels")

# Plot each channel with different colors
plt.plot(red_hist, color='red', label='Red')
plt.plot(green_hist, color='green', label='Green')
plt.plot(blue_hist, color='blue', label='Blue')

plt.xlim([0, 255])
plt.legend()
plt.show()

plt.hist(red_hist,color='red',label='red')
plt.hist(blue_hist,color='blue',label='blue')
plt.hist(green_hist,color='green',label='green')
plt.title("Colour Histogram")
plt.xlabel("Colour Value Range")
plt.ylabel("# of Pixels")
plt.legend()
plt.show()


# Audio section

import librosa
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

file_path='96.wav'
audio_data,sample_rate=librosa.load(file_path,sr=None)
time=librosa.times_like(audio_data,sr=sample_rate)
plt.plot(time, audio_data, color='b')
plt.title('Waveform of the Audio')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

speed=librosa.effects.time_stretch(y=audio_data,rate=2)
pitch=librosa.effects.pitch_shift(y=audio_data,sr=sample_rate,n_steps=3)
sf.write("Speed.mp3",speed,sample_rate)
sf.write("pitch.mp3",pitch,sample_rate)

delay=int(sample_rate*0.5)
echo=np.zeros_like(audio_data)
echo[delay:]=audio_data[:-delay]*0.5
audio_echo=audio_data+echo
sf.write('echo.mp3',audio_echo,sample_rate)

start=1
end=6
startSample=int(start*sample_rate)
endSample=int(end*sample_rate)
audio_trim=audio_data[startSample:endSample]
sf.write('trim.mp3',audio_trim,sample_rate)

silence=np.zeros(int(3*sample_rate))
audioSilence=np.concatenate((audio_data,silence))

noise=np.random.normal(0,0.1,audio_data.shape)
audioNoise=audio_data+noise

sf.write('Silence.mp3',audioSilence,sample_rate)
sf.write('noise.mp3',audioNoise,sample_rate)

stft=librosa.stft(audio_data)
spectrogram=np.abs(stft)
db_spectrogram=librosa.amplitude_to_db(spectrogram)

librosa.display.specshow(db_spectrogram, sr=sample_rate, x_axis='time', y_axis='log')
plt.title('Spectrogram')
plt.xlabel('Time(s)')
plt.ylabel('Frequency (Hz)')
plt.show()

