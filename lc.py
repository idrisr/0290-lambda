left  = lambda x: lambda y: x
right = lambda x: lambda y: y
def TRUE(x): return lambda y: x
def FALSE(x): return lambda y: y
AND    = lambda x: lambda y: x(y)(x)
OR     = lambda x: lambda y: x(x)(y)
NOT    = lambda x: x(FALSE)(TRUE)
incr   = lambda x: x+1
decr   = lambda x: x-1
CONS   = lambda a: lambda b: lambda s: s(a)(b)
CAR    = lambda s: s(TRUE)
CDR    = lambda s: s(FALSE)
T      = lambda p: CONS(SUCC(CAR(p)))(CAR(p))
ZERO   = lambda f: lambda x: x # take your f and stuff it
ONE    = lambda f: lambda x: f(x)
TWO    = lambda f: lambda x: f(f(x))
THREE  = lambda f: lambda x: f(f(f(x)))
FOUR   = lambda f: lambda x: f(f(f(f(x))))
ISZERO = lambda f: f(lambda x: FALSE)(TRUE)
SUCC   = lambda n: lambda f: lambda x: f(n(f)(x))
EXP    = lambda n: lambda f: lambda x: n(f)(x)
MUL    = lambda n: lambda f: lambda x: f(n(x))
ADD    = lambda x: lambda y: y(SUCC)(x)
SUB    = lambda x: lambda y: y(PRED)(x)
PRED   = lambda x: x(T)(CONS(ZERO)(ZERO))(FALSE)
FACT   = lambda n: ISZERO(n)(ONE)(MUL(n)(FACT(PRED(n))))

LAZY_TRUE = lambda x: lambda y: x()
LAZY_FALSE = lambda x: lambda y: y()
ISZERO = lambda n: n(lambda f: LAZY_FALSE)(LAZY_TRUE)
LFACT   = lambda n: ISZERO(n)\
                    (lambda: ONE)\
                    (lambda: MUL(n)(LFACT(PRED(n))))

#  (lambda f: lambda n:1 if n==0 else n*f(f)(n-1))\
#  (lambda f: lambda n:1 if n==0 else n*f(f)(n-1))(5))
