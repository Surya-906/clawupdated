import numpy as np
#generalized version
a=1
b=1
def xflux(x, y, u):
    return a*u

def yflux(x, y, u):
    return b*u

def advection_velocity(x,y):
    return (a,b)

# Upwind flux
def xnumflux(x, y, Fl, Fr, ul, ur):
    return Fl if a>0 else Fr

def ynumflux(x, y, Fl, Fr, ul, ur):
    return Fl if b>0 else Fr

# Return (1,1) at all points (x,y)
def local_speed(x, y, u):
    return (a*np.ones(x.shape), b*np.ones(x.shape))

def max_speed(x, y, u):
    return (abs(a), abs(b))
