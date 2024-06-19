import random
import unittest

def my_input(max_stage:int, size:int = random.randint(1, 200000)) -> list:
    input_list = [random.randint(1, max_stage+1) for _ in range(size)]
    print_input(input_list)
    return input_list

def print_input(arr:list):
    print(f"input_size={len(arr)} ex={arr[0]}")
    
class 실패율(unittest.TestCase):
    def test_simple(self):
        # given
        max_stage = 5
        stages = [2, 1, 2, 6, 2, 4, 3, 3]
    
        # when
        result = solution(max_stage, stages)
    
        # then
        self.assertEqual([3,4,2,1,5], result)
        
    def test_simple2(self):
        # given
        max_stage = 4
        stages = [4,4,4,4,4]
    
        # when
        result = solution(max_stage, stages)
    
        # then
        self.assertEqual([4,1,2,3], result)

    def test_(self):
        # given
        # max_stage = random.randint(1, 500)
        # input_list : list = my_input(max_stage)
        pass
    
        # when
    
        # then

def solution(max_stage:int, stages:list) -> list:
    # 총 사용자 수 저장
    total_user_count = len(stages)

    # 스테이지를 정렬 : 계수 정렬 (count sort) 사용
    new_list : list = [0] * (max(stages)+1)

    for item in stages:
        new_list[item] += 1

    result :dict = {}
    # 스테이지 1부터 순회하면서 실패율을 계산. 실패율 계산 시 하위 스테이지에 머물러있는 사용자는 제외
    for i in range(len(new_list)):
        # 해당 스테이지에 유저가 없는 경우
        if new_list[i] == 0:
            result[i] = 0
        # 유저가 있는 경우
        else:
            temp_user_count = new_list[i]
            result[i] = temp_user_count / total_user_count
            total_user_count -= temp_user_count
    
    if result.get(max_stage+1):
        result.pop(max_stage+1)
    result.pop(0)

    # 정렬 조건 : 실패율이 높은 스테이지 순으로 정렬. 실패율이 같은 경우 낮은 스테이지를 우선
    return [x[0] for x in sorted(result.items(), key=lambda x: (-x[1], x[0]))]

def quick_sort(arr:list, reverse:bool=False):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]
    
    left_side = [x for x in tail if __condition__(x, pivot, reverse)]
    right_side = [x for x in tail if __condition__(x, pivot, not reverse)]

    return quick_sort(left_side, reverse) + [pivot] + quick_sort(right_side, reverse)

def __condition__(x:int, pivot:int, reverse:bool=False):
    return __bigger__(x,pivot) if reverse else not __bigger__(x, pivot)

def __bigger__(x:list, pivot:list) -> bool:
    if x[1] > pivot[1]:
        return True
    elif x[1] < pivot[1]:
        return False

    if x[0] < pivot[0]:
        return True
    elif x[0] > pivot[0]:
        return False

unittest.main()