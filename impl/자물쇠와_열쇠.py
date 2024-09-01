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
    
    def test_test(self):
        ud = [(0,1), (0,2), (0,-1), (0,-2)]
        lr = [(-1,0), (-2,0) , (1,0), (2,0)]
        for i in ud:
            for j in lr:
                print(i, j)

def solution(key : list, lock : list) -> bool:
    # 1. 이동
    

    pass


if __name__ == '__main__':
    unittest.main()