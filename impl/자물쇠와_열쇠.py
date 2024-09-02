from itertools import combinations
import unittest

from move import move
from move_reverse import move_reverse

class Test(unittest.TestCase):
    def test_0(self):
        # given
        key = [[1, 0], [0, 0]]
        lock = [[1, 1], [1, 0]]
    
        # when
        result = solution(key, lock)
    
        # then
        self.assertTrue(result)
    
    # def test(self):
    #     # given
    #     key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    #     lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    #     # when
    #     result = solution(key, lock)

    #     # then
    #     self.assertTrue(result)



def solution(key : list, lock : list) -> bool:   
    hole_count = get_hole_count(lock)
    n = len(lock[0])
    m = len(key[0])

    conflict_cnt = 0
    match_cnt = 0

    key_idx_list = [[1,1], [1, 1]]
    lock_idx_list = [[0,0], [0,0]]
    
    key_result = apply(key, key_idx_list)
    lock_result = apply(lock, lock_idx_list)
    
    move_reverse(key_idx_list)

    return conflict_cnt == 0 and hole_count == match_cnt

def apply(arr, idx_list) -> list:
    s = idx_list[0]
    e = idx_list[1]
    return [arr[row][s[1]:e[1]+1] for row in range(s[0], e[0]+1)]

def get_hole_count(lock) -> int:
    hole_count = 0
    for row in lock:
        for e in row:
            if e == 0:
                hole_count += 1
    return hole_count


if __name__ == '__main__':
    unittest.main()