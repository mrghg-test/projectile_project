import matplotlib.pyplot as plt

def plot_xy(x, y):
    
    fig, ax1 = plt.subplots()
    
    ax1.plot(x, y)
    ax1.set_xlabel("x (m)")
    ax1.set_ylabel("y (m)")

    plt.show()

    
def plot_v(t, vx, vy):
    
    fig, ax1 = plt.subplots()
    
    ax1.plot(t, vx, label="x-velocity")
    ax1.plot(t, vy, label="y-velocity")

    plt.axhline(y=0, color="grey")

    ax1.set_xlabel("time (s)")
    ax1.set_ylabel("velocity (m/s)")

    ax1.legend()
    plt.show()