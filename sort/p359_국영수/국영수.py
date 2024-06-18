from copy import deepcopy
import random
import unittest

# def my_input(size:int = random.randint(1, 100000)) -> list:
def my_input(size:int = random.randint(1, 5000)) -> list:
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
        input_list = [[1, 10], [10, 10], [10, 1], [1, 9]]
        
        # when
        result = sort(input_list)
    
        # then
        self.assertEqual(result, [[10, 1], [10, 10], [1, 9], [1, 10]])
    
    def test_국영수(self):
        # given
    
        # when
        expected = sorted(input_list, key=lambda x: (-x[1], x[2], -x[3], x[0]))
        result = sort(input_list)
    
        # then
        self.assertEqual(result, expected)

def sort(arr:list) -> list:
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if smaller(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def smaller(arr1:list, arr2:list) -> bool:
    # 1. 국어는 내림
    # 2. 영어는 오름
    # 3. 수학은 내림
    # 4. 이름은 오름
    if len(arr1) == 2:
        return arr1[0] <= arr2[0] and arr1[1] >= arr2[1]

    if arr1[1] < arr2[1]:
        return True
    
    if arr1[1] == arr2[1] and arr1[2] > arr2[2]:
        return True
    
    if arr1[2] == arr2[2] and arr1[3] < arr2[3]:
        return True
    
    if arr1[3] == arr2[3] and arr1[0] > arr2[0]:
        return True
    
    return False

    # return arr1[1] <= arr2[1] and arr1[2] >= arr2[2] and arr1[3] <= arr2[3] and arr1[0] >= arr2[0]

unittest.main()