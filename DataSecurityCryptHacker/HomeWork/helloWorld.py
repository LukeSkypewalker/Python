from numpy import sin, pi, linspace
from pylab import plot, show, subplot, savefig

t = linspace(-pi, pi, 300)

subplot(2, 3, 1)
x = sin(t)
y = sin(t)
plot(x, y)

subplot(2, 3, 2)
x = sin(t + pi / 2)
y = sin(t)
plot(x, y)

subplot(2, 3, 3)
x = sin(t + pi/4)
y = sin(t)
plot(x, y)

subplot(2, 3, 4)
x = sin(2 * t)
y = sin(t + pi / 2)
plot(x, y)

subplot(2, 3, 5)
x = sin(3 * t + pi / 2)
y = sin(2 * t)
plot(x, y)

subplot(2, 3, 6)
x = sin(4 * t)
y = sin(3 * t + pi / 2)
plot(x, y)

savefig('Lissajous.png')
show()
