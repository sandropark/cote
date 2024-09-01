from itertools import combinations
import unittest

class Test(unittest.TestCase):
    def test(self):
        # given
        key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
        lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

        # when
        result = solution(key, lock)

        # then
        self.assertTrue(result)
    
def solution(key : list, lock : list) -> bool:   
    hole_count = get_hole_count(lock)
    n = len(lock[0])
    m = len(key[0])
    
    conflict_cnt = 0
    match_cnt = 0
    
    for i in range(n):
        inner_lock = lock[i]
        inner_key = key[i]
        for j in range(n):
            temp_lock = inner_lock[j]
            temp_key = inner_key[j]
            if temp_lock == 0 and temp_key == 1:
                match_cnt =+ 1
            elif temp_lock == 1 and temp_key == 1:
                conflict_cnt =+ 1

    return conflict_cnt == 0 and hole_count == match_cnt

def get_hole_count(lock) -> int:
    hole_count = 0
    for row in lock:
        for e in row:
            if e == 0:
                hole_count += 1
    return hole_count


if __name__ == '__main__':
    unittest.main()