import unittest

class Test(unittest.TestCase):
    def test_move_1(self):
        idx_list = [[0, 0], [0, 0]]

        moved = move_reverse(idx_list,3)
        self.assertFalse(moved)
        self.assertEqual(idx_list, [[0,0], [0,0]])
    
    def test_2(self):
        idx_list = [[2, 2], [2, 2]]

        moved = move_reverse(idx_list,3)
        self.assertTrue(moved)
        self.assertEqual(idx_list, [[2,1], [2, 2]])
    
    def test_2(self):
        idx_list = [[2, 1], [2, 2]]

        moved = move_reverse(idx_list,3)
        self.assertTrue(moved)
        self.assertEqual(idx_list, [[2,0], [2, 2]])
    
    def test_3(self):
        idx_list = [[0, 0], [2, 2]]

        moved = move_reverse(idx_list, 3)
        self.assertTrue(moved)
        self.assertEqual(idx_list, [[0, 2], [1, 2]])
    
    def test_4(self):
        idx_list = [[0, 0], [0, 2]]

        moved = move_reverse(idx_list, 3)
        self.assertTrue(moved)
        self.assertEqual(idx_list, [[0, 0], [0, 1]])
    
    
    def test_(self):
        lock = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        print_list(lock)
        
def print_list(arr):
    idx_list = [[2,2],[2,2]]

    print(get_arr(arr, idx_list))

    while move_reverse(idx_list, 3):
        print(get_arr(arr, idx_list))

def get_arr(arr, idx_list) -> list:
    s = idx_list[0]
    e = idx_list[1]
    return [arr[row][s[1]:e[1]+1] for row in range(s[0], e[0]+1)]

def move_reverse(idx_list : list, max_length:int) -> bool:
    s = idx_list[0]
    e = idx_list[1]
    if s[1] > 0:
        s[1] -= 1
        return True
    if s[0] > 0:
        s[0] -= 1
        s[1] = max_length -1
        return True
    if e[0] > 0:
        e[0] -= 1
        s[1] = max_length -1
        return True
    if e[1] > 0:
        e[1] -= 1
        return True

    return False

if __name__ == '__main__':
    unittest.main()