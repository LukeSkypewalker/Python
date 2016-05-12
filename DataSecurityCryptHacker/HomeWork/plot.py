from numpy import *
from matplotlib.pyplot import *


x = linspace(0, 2*pi, 256)
y1 = sin(x)
y2 = cos(x)
plot(x, y1, label="cosine")
plot(x, y2, label="sine")
grid()
xlabel('x')
ylabel('sin(x), cos(x)')
title('Sin & Cos')
legend(loc=1)
savefig('sin.png')
show()
