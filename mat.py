import  matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
a = 0
b = 0
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = [1, 2, 3]
ys = [2, 4, 1]

def animate(i, xs, ys):
    global a
    global b
    xs.append(a)
    ys.append(b)
    a = a+1
    b = b+3

    ax.clear()
    ax.plot(xs, ys, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=6) 
    plt.title("my sample graph")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=200)
plt.show()
    



