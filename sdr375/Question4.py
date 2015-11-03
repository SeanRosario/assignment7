#code for question 4
import numpy as np
import matplotlib.pyplot as plt


#@staticmethod
def q4():
    N_max = 50
    threshold = 50
    x, y= np.ogrid[-2:1:150j, -1.5:1.5:150j]
    c = x + 1j*y
    z = c
    print z
    for v in range(N_max):
        z = z**2 + c
    mask = np.abs(z) < threshold
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
