import pytest
import sys
sys.path.append('../search')
from binarysearch import  Binarysearch

def test_binarysearch():
    a=Binarysearch([1,2,3],2)
    