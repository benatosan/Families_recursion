#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Copy this cell into a new file for this question.

## Don't forget your libraries:
from typing import *
import check
import math

class Family:
    """Store information about the Family of a person.""" 
    name: str
    children: List['Family']

    def __init__(self, name: str, children: List['Family']):
        self.name = name
        self.children = children

    def __repr__(self) -> str:
        return "Family('{}', {})".format(self.name, self.children)

    
## Define your function here.
def farthest_child(fam: Family) -> List[str]:
    """return a list of names of fam leading to the farthest leaf, in order from leaf to start"""
    oldlist = []
    if fam.children == []:
        return [fam.name]
    else:
        for child in fam.children:
            result = []
            x = farthest_child(child)
            result.append(fam.name)
            result = x + result
            if len(oldlist) <= len(result):
                oldlist = result
    return oldlist 
        
                
## Here are some examples.
## If your solution does not pass these, your solution is definitely wrong!
## You are encouraged to include these examples as part of your solution.

## Start by thinking about a leaf:
check.expect("leaf", farthest_child(Family("Robb", [])), ["Robb"])
check.expect("leaf", farthest_child(Family("Sansa", [])), ["Sansa"])

tully = Family('Hoster',
                 [Family('Lysa',
                         [Family('Robin', [])]),
                  Family('Edmure', []),
                  Family('Catelyn',
                         [Family('Robb', []),
                          Family('Sansa', []),
                          Family('Arya', []),
                          Family('Bran', []),
                          Family('Rickon', [])])])
check.expect("tully", farthest_child(tully), ["Rickon", "Catelyn", "Hoster"])

example1 = Family('Ann',
                  [Family('Bob', [
                      Family('Cy', [Family('Di',[]),
                                    Family('Ed',[Family('Ollie', [])]),
                                    Family('Fox',[])]),
                      Family('Glen', [])]),
                   Family('Hi', [
                       Family('Io', [Family('Jo',[Family('Nat', [])]),
                                     Family('Kim',[]),
                                     Family('Li',[])]),
                       Family('Mo', [])])])

check.expect("ann", farthest_child(example1), 
             ["Nat", "Jo", "Io", "Hi", "Ann"])

## Don't forget to write your own tests as well!
## You may find it helpful to create a Family with just one child, or just two.
## You might base these families on the ones you have been given.
example2 = Family('Rob', [Family('Joe', [])])
check.expect("rob", farthest_child(example2), 
             ["Joe", "Rob"])

example3 = Family('Peter', [Family('Meg', []), Family('Stewie', [])])
check.expect("familyguy", farthest_child(example3), 
             ["Stewie", "Peter"])


# In[ ]:




