import numpy as np
import math
import matplotlib.pyplot as plt

def q_calc(x,n):
    answ = ((-1)*(x**2)*(2*n+1))/((2*n+2)*(2*n+3)*(2*n+3))
    return answ

def SI():
    xm = np.arange(0,2.1,0.4)
    e = 10**(-4)
    answer = list()
    j=0
    for x in xm:
        a0 = x
        Sum = a0
        i = 0
        while (True):
            qn = q_calc(x,i)
            ai = a0*qn
            Sum += ai
            a0 =ai
            i += 1
            if (abs(qn) < e):
                break
        Sum = Sum
        answer.append([x,Sum])
        j+=1
    print(answer)

poluch_znach = SI()

#print(poluch_znach)
# берем и считаем Ln(x) и потом вычисляем значения других функций
#Необходимо задать значение x
y_list = [0.0,0.3964614647513729,0.7720957854819964,1.1080471990137188,1.3891804858704384,1.6054129768026946]
x = np.array(np.arange(0,2.1,0.4), dtype=float)
y = np.array([0.0,0.3964614647513729,0.7720957854819964,1.1080471990137188,1.3891804858704384,1.6054129768026946], dtype=float)
xm = np.arange(0,2.1,0.4)/2

def _poly_newton_coefficient(x,y):
    """
    x: list or np array contanining x data points
    y: list or np array contanining y data points
    """

    m = len(x)

    x = np.copy(x)
    a = np.copy(y)
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(x[k:m] - x[k-1])

    return a

def newton_polynomial(x_data, y_data, x):
    """
    x_data: data points at x
    y_data: data points at y
    x: evaluation point(s)
    """
    a = _poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1 # Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -x_data[n-k])*p
    return p


newton_res = list(newton_polynomial(x,y,xm))
print(newton_polynomial(x,y,xm))
print("----------")
plt.plot(newton_res)
plt.plot(x)



#print(math.log(0.4))
def tr_integral(f,xmin,xmax,n):
    dx=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=dx*(f[i]+(f[i]+dx))/2
        x+=dx
    return area


print("tr_integral = {}".format(tr_integral(y_list,0,2,6)))
plt.show()