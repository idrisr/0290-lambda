from hypothesis.strategies import *
from hypothesis import given

def left(x): return lambda y: x
def right(x): return lambda y: y

@given(integers(), integers())
def test_left(a, b): assert left(a)(b) == a

@given(integers(), integers())
def test_right(a, b): assert right(a)(b) == b


#  left
#  right
#  NOT
#  TRUE
#  FALSE
#  AND
#  OR
#  0-4
#  succ
#  add
#  mul
