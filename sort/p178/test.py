from copy import deepcopy
import random
import unittest
from 위에서_아래로 import Sort

def my_input(order:int=0, size:int = random.randint(1, 500)) -> list:
    # return [random.randint(1, 100) for _ in range(size)]
    input_list = [random.randint(1, 100000) for _ in range(size)]
    print_input(order, input_list)
    return input_list

def print_input(order:int, arr:list):
    print(f"order={order}, input_size={len(arr)}, min={min(arr)}, max={max(arr)}")


class 위에서_아래로(unittest.TestCase):
    def test_select_sort(self):
        # given
        input_list : list = my_input(1)
        
        # when
        result : list = Sort.select_sort(deepcopy(input_list))
        expected : list = sorted(input_list, reverse=True)
    
        # then
        self.assertEqual(expected, result)

    def test_count_sort(self):
        # given
        input_list : list = my_input(2)
    
        # when
        result : list = Sort.count_sort(deepcopy(input_list))
    
        # then
        expected : list = sorted(input_list, reverse=True)
        self.assertEqual(expected, result)

unittest.main()