import pytest
import sys
sys.path.append('../')
from search import *
def test_linearSearch():
    a= linearSearch([1,3,2],2)
    assert a == 2
def test_binarySearch():
    a= binarySearch([1,3,2],3)
    assert a == 1
def test_binarySearch_2():
    a= binarySearch([1,3,2],4)
    assert a == -1
def test_jumpSearch():
    a= jumpSearch([1,3,2],4)
    assert a == -1
def test_fibonacciSearch():
    a= fibonacciSearch([1,3,2],4)
    assert a == -1
def test_exponentialSearch():
    a= exponentialSearch([1,3,2],4)
    assert a == -1
def test_interpolationSearch():
    a= interpolationSearch([1,3,2],4)
    
    assert a == -1
    
  