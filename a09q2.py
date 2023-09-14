#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Copy this cell into a new file for this question.

## Don't forget your libraries:
from typing import *
import check
import math

## We need this recursive data definition so we can refer to LLT.
LLT = Union[int, List['LLT']]

## Define your function here.
def tree_map(f: Callable, t: LLT) -> LLT:
    """Return an LLT with same shape as t but each leaf has been transformed by function f
    Requires: 
            f takes and returns an int
            t is not empty
    """
    if isinstance(t, int):
        return f(t)
    else:
        for num in range(0, len(t)):
            x = tree_map(f, t[num])
            if isinstance(x, int):
                t[num] = x
    return t
        
        
## Here are some examples.
## If your solution does not pass these, your solution is definitely wrong!
## You are encouraged to include these examples as part of your solution.

def add1(x: int) -> int: 
    """Return 1 more than x."""
    return x + 1
check.expect("add1:0", add1(5), 6)
check.expect("add1:1", add1(0), 1)

def sqr(x: int) -> int: 
    """Return the square of x."""
    return x*x
check.expect("sqr:0", sqr(2), 4)
check.expect("sqr:1", sqr(5), 25)

def double(n: int) -> int: 
    """Return twice n."""
    return n * 2
check.expect("double:0", double(4), 8)
check.expect("double:1", double(6), 12)

## We can now make some tests:
check.expect("TM1",
             tree_map(add1, [2, [[4], 6], 0, [1]]), 
             [3, [[5], 7], 1, [2]])
check.expect("TM2",
             tree_map(double, [2, [[4], 6], 0, [1]]), 
             [4, [[8], 12], 0, [2]])
check.expect("TM3", tree_map(sqr, 7), 49)
check.expect("TM4", tree_map(add1, [[[[[[[7]]]]]]]), 
             [[[[[[[8]]]]]]])   


## Don't forget to write your own tests as well!

check.expect("TM5", tree_map(double, 0), 0)
check.expect("TM6", tree_map(sqr, [16, [[9], 4], 4, [4]]), [256, [[81], 16], 16, [16]])


# In[ ]:




