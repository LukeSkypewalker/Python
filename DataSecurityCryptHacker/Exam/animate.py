import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def update(i):
    global scan, data
    scan.set_ydata(data[i])
    return scan, 
# ASK
def animate(path, fov):
    global scan, data
    data = np.load(path)
    fig = plt.figure(figsize=(19.2, 10.8))
    ax = plt.subplot(111, projection='polar')
    angles = np.radians(np.linspace(-fov/2, fov/2, data.shape[1]))
    scan = ax.plot(angles, data[0], '.')[0]
    ax.set_rmax(5000)
    ax.grid(True)
    ani = animation.FuncAnimation(fig, update, frames=len(data))
    plt.show()

if __name__ == '__main__':
    animate('test_data/data.npy', 240)