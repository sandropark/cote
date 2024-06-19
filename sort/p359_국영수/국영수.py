import random
import unittest

def my_input(size:int = random.randint(1, 100000)) -> list:
    input_list = [[make_name(), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)] for _ in range(size)]
    print_input(input_list)
    return input_list

def make_name()->str:
    return ''.join([chr(random.randint(97, 122)) for _ in range(random.randint(1, 10))])

def print_input(arr:list):
    print(f"input_size={len(arr)} ex={arr[0]}")

input_list : list = my_input()

class 국영수(unittest.TestCase):
    def test_simple(self):
        # given
        input_list = [[0, 1, 10], [0, 10, 10], [0, 10, 1], [0, 1, 9]]
        
        # when
        actual = quick_sort(input_list, True)
    
        # then
        self.assertEqual([[0, 10, 1], [0, 10, 10], [0, 1, 9], [0, 1, 10]], actual)
    
    def test_국영수(self):
        # given
        # print(f'input={input_list}')
    
        # when
        expected = sorted(input_list, key=lambda x: (-x[1], x[2], -x[3], x[0]))
        # print(f'expected={expected}')
        actual = quick_sort(input_list, True)
        # print(f'actual={actual}')
    
        # then
        self.assertEqual(expected, actual)
    
    def test_2(self):
        # given
        input_list = [['k', 96, 46, 31], 
                      ['ad', 59, 50, 21], 
                      ['klaw', 97, 13, 31], 
                      ['lvzcquq', 32, 52, 85], 
                      ['d', 47, 52, 18], 
                      ['csnfcjygq', 35, 73, 65], 
                      ['fvklhbjw', 36, 39, 56], 
                      ['clccorjsje', 5, 53, 51], 
                      ['mtufcwf', 42, 52, 52], 
                      ['vlp', 29, 42, 30]]
    
        # when
        actual = quick_sort(input_list, True)
    
        # then
        self.assertEqual([['klaw', 97, 13, 31], 
                          ['k', 96, 46, 31], 
                          ['ad', 59, 50, 21], 
                          ['d', 47, 52, 18], 
                          ['mtufcwf', 42, 52, 52], 
                          ['fvklhbjw', 36, 39, 56], 
                          ['csnfcjygq', 35, 73, 65], 
                          ['lvzcquq', 32, 52, 85], 
                          ['vlp', 29, 42, 30], 
                          ['clccorjsje', 5, 53, 51]] ,actual)

def quick_sort(arr:list, reverse:bool=False):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]
    
    left_side = [x for x in tail if __condition__(x, pivot, reverse)]
    right_side = [x for x in tail if __condition__(x, pivot, not reverse)]

    return quick_sort(left_side, reverse) + [pivot] + quick_sort(right_side, reverse)

def __condition__(x:list, pivot:list, reverse:bool=False) -> bool:
    return __bigger__(x, pivot) if reverse else not __bigger__(x, pivot)

def __bigger__(x:list, pivot:list) -> bool:
    if x[1] > pivot[1]:
        return True
    elif x[1] < pivot[1]:
        return False

    if x[2] < pivot[2]:
        return True
    elif x[2] > pivot[2]:
        return False

    if x[3] > pivot[3]:
        return True
    elif x[3] < pivot[3]:
        return False

    if x[0] < pivot[0]:
        return True
    elif x[0] > pivot[0]:
        return False
    return False

unittest.main()