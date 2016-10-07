from math import sin, cos
import matplotlib.pyplot as plt
from openpyxl import Workbook

fig = plt.figure()


k=2

def u(x):
    return sin(2*x)-cos(x)

def du(x):
    return 2 * cos(2 * x) + sin(x)

def f(x,y):
    return du(x)+k*(y-u(x))

def PlotU(x0,fig):
    x = [x0]
    y=[u(x0)]
    for i in range(N):
        x0 += h
        x.append(x0)
        y.append(u(x0))
    au = fig.add_subplot(111)
    au.plot(x, y, 'o-')
    ##plt.show()

def Output(x0,N,h):
    f = open("PK.txt", "w")
    f.write("Function: "+'\n')
    for i in range(N+1):
        f.write(str(u(x0)) + " ")
        x0 +=h
    f.close()

def PK(h,x0,N):

    y0 = u(x0)
    y = [y0] ## ZERO
    x = x0

    for i in range(N):
        ##print (i)
        la = 0.05
        k = la*2
        yi = y0 + h * f(x, y0) ## находим y(i+1) итерация - 0 ## ONE
        y.append(yi)        ## добавляем в список
        ys=yi
        s = 0
        ##############
        while  k>la:

           ## print (s)
            y[i+1]=y[i] + h * ( f(x,y[i]) + f(x+h,ys) ) / 2
            k=abs( (y[i+1]-ys)/ys )

            ys = y[i + 1]
            s +=1 ##
        ################

        x = x + h   ## переходим к x(i+1)
        y0 = yi   ## становимся на y(i+1)

    return y

def PlotPK(x0,h,N,y):
    x=[x0]
    for i in range (N):
        x0+=h
        x.append(x0)
    ax = fig.add_subplot(111)
    ax.plot(x, y, 'o-')
    plt.show()

def PkOut(y,x0):
    f = open("PK.txt", "a")
    f.write('\n'+"Counted: " + '\n')
    for i in y:
        f.write(str(i) + " ")
        x0 += h
    f.close()

def CountError(y,x0,h):
    E=[]
    for item in y:
        e=abs(item-u(x0))
        E.append(e)
        x0 +=h
    return E

def ErrorOut(E):
    fl = open("PK.txt", "a")
    fl.write('\n' + "Error:"+'\n')
    for item in E:
        fl.write(str(item) + " ")
    fl.write('\n'+"Absolute:"+'\n')
    fl.write(str(max(E)))
    fl.close()

N= int(input("Введите кол-во точек: "))
N -=1

x0 = 0 #int(input("Введите левую границу интервала: "))
xN = 3 #int(input("Введите правую границу интервала: "))
h=(xN-x0)*1.0/N

Output(x0,N,h)
PlotU(x0,fig)
y=(PK(h,x0,N))
PkOut(y,x0)
PlotPK(x0,h,N,y)
ErrorOut(CountError(y,x0,h))



