
import numpy as np
import scipy.integrate as integrate
import sys
import matplotlib.pyplot as plt
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


def GaussLagRule(n,func):
   value = 0
   x, w = np.polynomial.laguerre.laggauss(int(n))
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
    if '--trapezodial' in sys.argv:
        p = sys.argv.index('--trapezodial')
        dotrapz = bool(sys.argv[p])

    if '--gausquad' in sys.argv:
            p = sys.argv.index('--gausquad')
            dogausquad = bool(sys.argv[p])
    if '-h' in sys.argv or '--help' in sys.argv:
            print ("Usage: %s [-function] function [-limit] lowlimit uplimit [-step] number [--trapezodial] [--gausquad] " % sys.argv[0])
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
