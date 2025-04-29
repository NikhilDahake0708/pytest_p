import pytest

#defining a function with parameter x
# def func(x):
#   return x+5

@pytest.fixture
def input_value():
   input = 8
   return input

#defining an another function 
def test_method(input_value):
 #check whether 3+5 = 5 or not by passing 3 as an argument in function x
  assert input_value == 8
