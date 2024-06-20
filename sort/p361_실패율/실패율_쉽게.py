
import unittest
    
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

    def test_3(self):
        # given
        max_stage = 2
        stages = [1,1,1,1]    
    
        # when
        result = solution(max_stage, stages)
    
        # then
        self.assertEqual([1,2], result)

def solution(max_stage:int, stages:list) -> list:
    total_user_count = len(stages)

    new_list : list = [0] * (max_stage + 2)

    for item in stages:
        new_list[item] += 1

    for i in range(len(new_list)):
        temp_user_count = new_list[i]
        if temp_user_count != 0:
            new_list[i] = temp_user_count / total_user_count
            total_user_count -= temp_user_count
    
    return [x[0] 
            for x in sorted(enumerate(new_list), key=lambda x: (-x[1], x[0])) 
            if x[0] != 0 and x[0] <= max_stage]

unittest.main()