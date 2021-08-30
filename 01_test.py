from hypothesis.strategies import *
from hypothesis import given

def NOT(x):   return x(FALSE)(TRUE)
def TRUE(x):  return lambda y: x
def FALSE(x): return lambda y: y
def AND(x):   return lambda y: x(y)(x)
def OR(x):    return lambda y: x(x)(y)
def left(a):  return lambda b: a
def right(a): return lambda b: b
ONE   = lambda f: lambda x: f(x)
TWO   = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR  = lambda f: lambda x: f(f(f(f(x))))
ZERO  = lambda f: lambda x: x
SUCC  = lambda n: lambda f: lambda x: f(n(f)(x))
ADD = lambda x: lambda y: y(SUCC)(x)
MUL = lambda x: lambda y: lambda f: y(x(f))

@given(integers(), floats(allow_nan=False))
def test_left(a, b): assert left(a)(b) == a

@given(integers(), floats(allow_nan=False))
def test_right(a, b): assert right(a)(b) == b
