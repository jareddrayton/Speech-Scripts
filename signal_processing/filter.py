import numpy as np
import scipy.io.wavfile as wav

(rate, signal) = wav.read("Sounds/{!s}".format("test_a.wav"))

print(rate, signal)
print(type(signal))




def lowpass(audio):
    
    # either pad by size of tap or truncate
    
    tap_size = 5

    processed_audio = []

    #print(np.append(audio, [tap_size*0]))

    for i in range(0, len(audio)-tap_size):
        processed_audio.append(sum(map(lambda x:x//tap_size, audio[i:i+tap_size])))

    print(np.array(processed_audio[:100]))

    return(processed_audio[:100])


print(signal[:100])
lowpass(signal)


 