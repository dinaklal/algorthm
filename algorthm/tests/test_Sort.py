import pytest
import sys
sys.path.append('../')
from sort import *
def test_bubbleSort():
    a= bubbleSort([1,3,2])
    assert a == [1,2,3]
def test_mergeSort():
    a= mergeSort([1,3,2])
    assert a == [1,2,3]
def test_insertionSort():
    a= insertionSort([1,3,2])
    assert a == [1,2,3]
def test_shellSort():
    a= shellSort([1,3,2])
    assert a == [1,2,3]
def test_selectionSort():
    a= selectionSort([1,3,2])
    assert a == [1,2,3]
def test_bubbleSort_without_steps():
    a= bubbleSort([1,3,2],False)