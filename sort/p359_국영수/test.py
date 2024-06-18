from copy import deepcopy
import random
import unittest

def my_input(size:int = random.randint(1, 500)) -> list:
    # return [random.randint(1, 100) for _ in range(size)]
    input_list = [random.randint(1, 100000) for _ in range(size)]
    print_input(input_list)
    return input_list

def print_input(arr:list):
    print(f"input_size={len(arr)}, min={min(arr)}, max={max(arr)}")
    
input_list : list = my_input(3)

class 국영수(unittest.TestCase):
    def test_a(self):
        # given
        pass
    
        # when
    
        # then
        
unittest.main()