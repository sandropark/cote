import random
import unittest

def my_input(size:int = random.randint(1, 200000)) -> list:
    input_list = [random.randint(1, 100000) for _ in range(size)]
    print_input(input_list)
    return input_list

def print_input(arr:list):
    print(f"input_size={len(arr)} ex={arr[0]}")

input_list : list = my_input()

class 안테나(unittest.TestCase):
    def test_simple(self):
        # given
        input_list = [5, 1, 7, 9]
    
        # when
        actual = solution(input_list)
    
        # then
        self.assertEqual(5, actual)
    
def solution(arr:list) -> int:
    # 리스트의 평균을 구한다.
    avg = sum(arr)/len(arr)
    # 리스트를 정렬한다.
    
    sorted_list = quick_sort(arr)
    # 평균에 가장 가까운 값을 찾는다. 여러 개라면 더 작은 값이 우선
    
    for i in range(len(sorted_list)-1):
        temp = sorted_list[i]
        if temp == avg:
            return temp
        if temp < avg < sorted_list[i+1]:
            a = avg - temp
            b = sorted_list[i+1] - avg
            return temp if a < b else sorted_list[i+1]
    pass

def quick_sort(arr:list, reverse:bool=False):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]
    
    left_side = [x for x in tail if __condition__(x, pivot, reverse)]
    right_side = [x for x in tail if __condition__(x, pivot, not reverse)]

    return quick_sort(left_side, reverse) + [pivot] + quick_sort(right_side, reverse)

def __condition__(x:int, pivot:int, reverse:bool=False):
    return x > pivot if reverse else x <= pivot

unittest.main()