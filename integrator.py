
import numpy as np
import scipy.integrate as integrate
import sys
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import sympy as sympy


sys.path.append(".")
def Trapez(f,n,a,b):
   h = (b-a)/float(n)
   s = 0
   x = a
   for i in range(1,int(n),1):
       x = x+h
       s = s+ f(x)
   s = 0.5*(f(a)+f(b)) +s
   return h*s


def GaussLagRule(n,func,a,b):
   value = 0
   x, w = np.polynomial.legendre.laggauss(int(n))

   for i in range(1,int(n),1):
       value = value+ (func(x[i])*np.exp(x[i]))*w[i]
   return value



def default_func(x):
    return x*x*np.exp(-x)
def default_funcsympy(x):
    return x*x*sympy.exp(-x)


def Symbolic(func,a,b):
    x =  sympy.Symbol('x')
    value = sympy.integrate(func(x),(x,a,sympy.oo))
    return value

if __name__ == "__main__":
    step = 10.
    a = 0.
    b = 10
    dotrapz = False
    dogausquad = False
    doplot = False
    if '-function' in sys.argv:
        p = sys.argv.index('-function')
        func = int(sys.argv[p+1])
    if '-limit' in sys.argv:
        p = sys.argv.index('-limit')
        a = int(sys.argv[p+1])
        b = int(sys.argv[p+2])
    if '-step' in sys.argv:
        p = sys.argv.index('-step')
        step = int(sys.argv[p+1])
    if '--trapezoidal' in sys.argv:
        p = sys.argv.index('--trapezoidal')
        dotrapz = bool(sys.argv[p])

    if '--gausquad' in sys.argv:
            p = sys.argv.index('--gausquad')
            dogausquad = bool(sys.argv[p])
    if '--plot' in sys.argv:
            p = sys.argv.index('--plot')
            doplot = bool(sys.argv[p])
    if '-h' in sys.argv or '--help' in sys.argv:
            print ("Usage: %s [-function] function [-limit] lowlimit uplimit [-step] number [--trapezoidal] [--gausquad] [--plot] " % sys.argv[0])
            print
            sys.exit(1)

    if dotrapz:
        testinteg = Trapez(default_func,step,a,b)
        gaus = GaussLagRule(step,default_func)
        analytic = Symbolic(default_funcsympy,a,b)
        print( f"Integration with Trapezoidal Rule a= {a} b = {b} and n = {step}: ",testinteg)
        print (f"integration with Gaussian-Quadrature n ={step}: ", gaus)
        print ("Analytic Integration: ",analytic)
    else:
        print("no integration rule defined")
    if doplot:
        fig = plt.figure(figsize=(8,3))

        x = list(np.arange(1,10,0.05))
        y = list(map(default_func,x))
        x_gauss, w_gauss = np.polynomial.laguerre.laggauss(int(step))

        plt.plot(x,y,color='green')
        second_plot, = plt.plot(x_gauss,w_gauss,color="red")
        print (second_plot,w_gauss[0])
        slider_ax = plt.axes([0.1, 0.005, 0.8, 0.05])
        slide = Slider(slider_ax,      # the axes object containing the slider
                  'a',            # the name of the slider parameter
                  1,          # minimal value of the parameter
                  100,          # maximal value of the parameter
                  valinit=1  # initial value of the parameter
                 )
        def update(a):
            x_ch , y_ch = np.polynomial.laguerre.laggauss(int(a))
            second_plot.set_ydata(y_ch)
            second_plot.set_xdata(x_ch)

            fig.canvas.draw_idle()
        slide.on_changed(update)
        plt.show()
