from itertools import combinations
import unittest

class Test(unittest.TestCase):
    def test(self):
        # given
        input = [3,2,1,1,9]
        
        # when
        result = solution(input)

        # then
        self.assertEqual(result, 8)

def solution(input:list) -> int:
    found : bool
    for i in range(1, sum(input)+1):
        found = True
        if contains(input, i):
            found = False
            continue
        for r in range(2, len(input)):
            combi = list(set(map(sum, combinations(input, r))))
            if contains(combi, i):
                found = False
                break
        if found:
            return i

def contains(arr:list, target:int) -> bool:
    return arr.count(target) != 0


if __name__ == '__main__':
    unittest.main()