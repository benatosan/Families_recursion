#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Copy this cell into a new file for this question.

## Don't forget your libraries:
from typing import *
import check
import math

## Modify this function.
def find_fixed_point(f: Callable, x0: float, threshold: float) -> float:
    """Starting at x0, iterate f until f(x0) and x0
    differ by no more than threshold.
    Requires: 
        f must converge eventually
        threshold >= 0
    """    
    if abs(x0-f(x0)) <= threshold:
        return f(x0)
    else:
        return find_fixed_point(f, f(x0), threshold)

## Here are some examples.
## If your solution does not pass these, your solution is definitely wrong!
## You are encouraged to include these examples as part of your solution.

def improve_sqrt3(g: float) -> float:
    """With g being a guess for sqrt(3), return a better guess."""
    return (g + 3.0 / g) / 2.0

check.within("sqrt3,1", improve_sqrt3(3.0), 2.0, 0.0001)
check.within("sqrt3,2", improve_sqrt3(1.0), 2.0, 0.0001)
check.within("sqrt3,3", improve_sqrt3(1000000.0), 500000.0, 0.0001)


def digit_sum(n: int) -> int:
    """Return the sum of the digits of n.
    Requires: n >= 0.
    """
    if n > 0:
        return n % 10 + digit_sum(n // 10)
    else:
        return 0

check.expect("DS999...", digit_sum(999999999999993), 129)
check.expect("DS129", digit_sum(129), 12)
check.expect("DS12", digit_sum(12), 3)
check.expect("DS3", digit_sum(3), 3)

def approach10(n: int) -> int:
    """If n is a multiple of 10, return it; otherwise, return 1 less."""
    if n % 10 == 0:
        return n
    else:
        return n - 1

check.expect("43->42", approach10(43), 42)
check.expect("30->30", approach10(30), 30)


check.within("FQ2", 
             find_fixed_point(improve_sqrt3, 5.0, 0.00001), 
             1.732, 0.0001)
check.within("FQ3", find_fixed_point(improve_sqrt3, 3.0, 1.0), 2.0, 0.0001)
check.expect("FD1", find_fixed_point(digit_sum, 999999999999993, 0.0), 3)
check.within("Fsqrt", find_fixed_point(math.sqrt, 1000, 0.00001), 1.0, 0.0001)
check.expect("A10", find_fixed_point(approach10, 42, 0.00001), 40)
check.within("Aabs", find_fixed_point(abs, -2, 0.0), 2, 0.0)
check.within("Asin", find_fixed_point(math.sin, 0.0, 0.0001), 0.0, 0.0001)

## Solution to x = cos(x), which is the Dottie number:
## https://mathworld.wolfram.com/DottieNumber.html
check.within("Ad", find_fixed_point(math.cos, 1.0, 0.00001), 0.739085, 0.0001)
check.expect("FD1", find_fixed_point(digit_sum, 999999999999993, 0.0), 3)

check.within("Ad2", find_fixed_point(math.cos, 2.0, 0.00001), 0.739085, 0.0001)
check.within("FQ4", find_fixed_point(improve_sqrt3, 7.0, 0.0001), 1.732, 0.0001)

## Don't forget to write your own tests as well!
## You could use the tests you used on the previous assignment.

