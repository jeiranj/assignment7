import numpy as np
import matplotlib.pyplot as plt
import warnings

def exec_module():
    # Draw Mandelbrot fractal.
    print '\n\n***Question 4*** \n'
    np.seterr(all='warn')
    warnings.simplefilter("ignore", RuntimeWarning) 
    x = np.arange(-2.,1,0.005)
    x = x.reshape(len(x),1)
    y = np.arange(-1.5,1.5,0.005)
    y = y.reshape(1,len(y))
    c = x + 1j*y
    N_max = 50
    threshold = 50
    z = c
    for v in range(N_max):
        z=z**2+c
    mask = np.float64(abs(z) < threshold)
    
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5],cmap='hot')
    plt.gray()
    plt.savefig('mandelbrot.png')
    
if __name__ == '__main__':
    exec_module()