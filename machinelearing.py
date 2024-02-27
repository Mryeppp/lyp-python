import math
import matplotlib.pyplot 

if __name__ == '__main__':
    x = [float(1)/100.0 for i in range(1, 300)]
    y = [math.log(i) for i in x]
    matplotlib.pyplot .plot(x, y, 'r-', linewidth=3, label='log Curve')
    a = [x[20], x[175]]
    b = [y[20], y[175]]
    matplotlib.pyplot.plot(a, b, 'g-', linewidth=2)
    matplotlib.pyplot.plot(a, b, 'b', markersize=15, alpha=0.75)  # Changed 'b=' to 'bo'
    matplotlib.pyplot.legend(loc='upper left')
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.xlabel('X')
    matplotlib.pyplot.ylabel('log(x)')
    matplotlib.pyplot.show()

