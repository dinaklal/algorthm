import pytest
import sys
sys.path.append('../')
from search import *
def test_linearSearch():
    a= linearSearch([1,3,2],4)
    assert a == -1
  