# import modules
import numpy as np
import matplotlib.pyplot as plt

#----- define Lorenz system
def lorenz(x, y, z, b = 8/3, s = 10, r = 28): #setting parameters
    dx_dt = s*(y - x) #ODEs
    dy_dt = x*(r - z) - y
    dz_dt = x*y - b*z
    return dx_dt, dy_dt, dz_dt #returns Lorenz attractor's time derivatives at x, y, z

#time difference and number of steps
dt = 0.01
steps = 10000

#setting initial conditions
xs = np.empty(steps + 1)
ys = np.empty(steps + 1)
zs = np.empty(steps + 1)
xs[0], ys[0], zs[0] = (2.01, 5, 20)

#time array for plotting
t = np.arange(0, steps*dt + dt, dt)  #array of time points from 0 to steps*dt

#calculate derivatives at each time point/step
for i in range(steps):
    dx_dt, dy_dt, dz_dt = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + dx_dt*dt
    ys[i + 1] = ys[i] + dy_dt*dt
    zs[i + 1] = zs[i] + dz_dt*dt

#-----plotting
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

#plot Lorenz Attractor in 3d
axs[0] = fig.add_subplot(2, 1, 1, projection='3d')
axs[0].plot(xs, ys, zs, lw=0.5)
axs[0].set_xlabel("x axis")
axs[0].set_ylabel("y axis")
axs[0].set_zlabel("z axis")
axs[0].set_title("Lorenz Attractor rho=28")

#plot x and z against t on same graph
axs[1].plot(t, zs, label='z', color='red', lw=0.5)   #plot z against time
axs[1].plot(t, xs, label='x', color='blue', lw=0.5)  #plot x against time
axs[1].set_xlabel("Time")
axs[1].set_ylabel("Value")
axs[1].set_title("x and z vs time")
axs[1].legend()

plt.tight_layout()
plt.savefig('lorentz_r_28_plots.pdf')
plt.show()
