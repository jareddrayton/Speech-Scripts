import matplotlib.pyplot as plt
import math

sample_rate = 44100
ts = 1 / sample_rate
frequency = 120

buffer = []

for n in range(sample_rate):
    print(math.sin(2 * math.pi * frequency * n * ts))
    buffer.append(math.sin(2 * math.pi * frequency * n * ts))

fig, ax = plt.subplots()
ax.plot(buffer)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()