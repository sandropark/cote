import unittest

class Test(unittest.TestCase):
    def test_move_1(self):
        idx_list = [[0, 0], [0, 0]]

        move(idx_list, 3)
        self.assertEqual(idx_list, [[0,0], [0,1]])

    def test_2(self):
        idx_list = [[0, 0], [0, 1]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[0,0], [0,2]])

    def test_3(self):
        idx_list = [[0, 0], [0, 2]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[0,1], [0,2]])
        
    def test_4(self):
        idx_list = [[0, 1], [0, 2]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[0,2], [0,2]])

    def test_5(self):
        idx_list = [[0, 2], [0, 2]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[0,0], [1,0]])

    def test_6(self):
        idx_list = [[0, 0], [1, 0]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[0,0], [1,1]])
    
    def test_7(self):
        idx_list = [[0, 0], [1, 1]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[0,0], [1,2]])

    def test_8(self):
        idx_list = [[0, 0], [1, 2]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[0,1], [1,2]])
    
    def test_9(self):
        idx_list = [[0, 1], [1, 2]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[0,2], [1,2]])
    
    def test_10(self):
        idx_list = [[0, 2], [1, 2]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[0,0], [2,0]])
        
    def test_11(self):
        idx_list = [[0, 2], [2, 2]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[1,0], [2,0]])
    
    def test_99(self):
        idx_list = [[2, 2], [2, 2]]
        move(idx_list, 3)
        self.assertEqual(idx_list, [[2,2], [2,2]])


def move(idx_list : list, max_length: int) -> bool:
    s = idx_list[0]
    e = idx_list[1]
    if e[1] < max_length-1:
        e[1] += 1
        return True
    if s[1] < max_length-1:
        s[1] += 1
        return True
    if e[0] < max_length-1:
        e[0] += 1
        e[1] = 0
        s[1] = 0
        return True
    if s[0] < max_length-1:
        s[0] += 1
        s[1] = 0
        e[1] = 0
        return True
    return False

def move_reverse(idx_list : list, max_length: int) -> bool:
    pass


if __name__ == '__main__':
    unittest.main()