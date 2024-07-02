import unittest

# 고정점: 수열의 원소 중에서 그 값이 인덱스와 동일한 원소

class Test(unittest.TestCase):
    def test_1(self):
        # given
        n = 5
        arr = [-15, -6, 1, 3, 7]

        # when
        result = binary_search(arr, 0, n-1)
        
        # then
        self.assertEqual(result, 3)
    
    def test_2(self):
        # given
        n = 7
        arr = [-15, -4,2,8,9,13,15]

        # when
        result = binary_search(arr, 0, n-1)
        
        # then
        self.assertEqual(result, 2)
    def test_3(self):
        # given
        n = 7
        arr = [-15, -4,3,8,9,13,15]

        # when
        result = binary_search(arr, 0, n-1)
        
        # then
        self.assertEqual(result, -1)


def binary_search(arr:list, start_idx:int, end_idx:int)->int:
    if start_idx > end_idx:
        return -1
    center_idx = (end_idx-start_idx) // 2 + start_idx
    center_element = arr[center_idx]

    if center_element == center_idx:
        return  center_idx
    elif center_idx > center_element:
        return binary_search(arr, center_idx+1, end_idx)
    elif center_idx < center_element:
        return binary_search(arr, start_idx, center_idx-1)
    



if __name__ == '__main__':
    unittest.main()