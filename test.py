from hypothesis.strategies import *
from hypothesis import given
import pytest
from lc import *


@given(integers(), integers())
def test_left(a, b): assert left(a)(b) == a

@given(integers(), integers())
def test_right(a, b): assert right(a)(b) == b

@pytest.mark.parametrize("a,b,exp", [
    (TRUE,  TRUE,  TRUE),
    (TRUE,  FALSE, FALSE),
    (FALSE, TRUE,  FALSE),
    (FALSE, FALSE, FALSE), ])
def test_and(a, b, exp):
    assert AND(a)(b) == exp

@pytest.mark.parametrize("a,b,exp", [
    (TRUE,  TRUE,  TRUE),
    (TRUE,  FALSE, TRUE),
    (FALSE, TRUE,  TRUE),
    (FALSE, FALSE, FALSE), ])
def test_or(a, b, exp):
    assert OR(a)(b) == exp

@pytest.mark.parametrize("a,exp", [
    (TRUE,  FALSE),
    (FALSE, TRUE), ])
def test_or(a, exp):
    assert NOT(a) == exp

@given(integers())
def test_zero(a):  assert ZERO(incr)(a) == a
@given(integers())
def test_one(a):   assert ONE(incr)(a) == a + 1
@given(integers())
def test_two(a):   assert TWO(incr)(a) == a + 2
@given(integers())
def test_three(a): assert THREE(incr)(a) == a + 3
@given(integers())
def test_four(a):  assert FOUR(incr)(a) == a + 4

@given(integers(), sampled_from([ZERO, ONE, TWO, THREE, FOUR]))
def test_succ(a, f):  assert SUCC(f)(incr)(a) == f(incr)(a) + 1

@given(integers() | floats(allow_nan=False), 
        sampled_from([ZERO, ONE, TWO, THREE, FOUR]),
        sampled_from([ZERO, ONE, TWO, THREE, FOUR]))
def test_add(a, g, f):  
    assert ADD(g)(f)(incr)(a) == ADD(f)(g)(incr)(a)
    assert ADD(g)(ZERO)(incr)(a) == g(incr)(a)
    assert ADD(f)(ZERO)(incr)(a) == f(incr)(a)

#  @given(integers() | floats(allow_nan=False), 
        #  sampled_from([ZERO, ONE, TWO, THREE, FOUR]),
        #  sampled_from([ZERO, ONE, TWO, THREE, FOUR]))
#  def test_sub(a, g, f):  
    #  assert ADD(f)(SUB(g)(f))(incr)(a) == g(incr)(a)

@given(integers() | floats(allow_nan=False), 
        sampled_from([ZERO, ONE, TWO, THREE, FOUR]),
        sampled_from([ZERO, ONE, TWO, THREE, FOUR]))
def test_mul(a, g, f):  
    assert MUL(g)(f)(incr)(a) == MUL(f)(g)(incr)(a)
    assert MUL(ZERO)(f)(incr)(a) == a
    assert MUL(ZERO)(g)(incr)(a) == a

@given(integers(), integers())
def test_cons(a, b):
    p = CONS(a)(b)
    assert CAR(p) == a
    assert CDR(p) == b

@given(sampled_from([ZERO, ONE, TWO, THREE, FOUR]),
       sampled_from([ZERO, ONE, TWO, THREE, FOUR]),
       integers() | floats(allow_nan=False))
def test_T(f, g, a):
    if f == ZERO:
        assert CDR(f(T)(CONS(g)(g)))(incr)(a) == CAR(f(T)(CONS(g)(g)))(incr)(a)
    else:
        assert CDR(f(T)(CONS(g)(g)))(incr)(a) + 1 == CAR(f(T)(CONS(g)(g)))(incr)(a)


@given(sampled_from([ONE, TWO, THREE, FOUR]), 
        integers())
def test_pred(f, a):
    assert PRED(f)(incr)(a) == f(incr)(a) - 1
    assert SUCC(PRED(f))(incr)(a) == f(incr)(a)
