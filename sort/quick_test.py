import unittest
import quick

class QuickTest(unittest.TestCase):
    # 피벗보다 큰 수의 인덱스를 찾는다.
    def test_find_left_idx(self):
        # given
        arr = [3,4,2,8,5,9,0,1,6,7]

        pivot_idx, left_idx = 0, 1

        # when
        result = quick.find_left_idx(arr, pivot_idx, left_idx, end=9)

        #then
        self.assertEqual(result, 1)
    
    # 피벗 왼쪽에 피벗보다 큰 수가 없는 경우 left_idx는 리스트의 마지막 인덱스에서 멈춘다.
    def test_find_left_idx2(self):
        # given
        arr = [3, 2, 1]
        
        # when
        result = quick.find_left_idx(arr, pivot_idx=0, temp_left_idx=1, end=2)

        #then
        self.assertEqual(result, 2)
        
    # 피벗보다 작은 수의 인덱스를 찾는다.
    def test_find_right_idx(self):
        # given
        arr = [3,4,2,8,5,9,0,1,6,7]

        pivot_idx, right_idx = 0, len(arr)-1

        # when
        result = quick.find_right_idx(arr, pivot_idx, right_idx)

        #then
        self.assertEqual(result, 7)
    
    # right_idx는 0이하가 될 수 없다.
    def test_find_right_idx2(self):
        # given
        arr = [1,2,3]

        # when
        result = quick.find_right_idx(arr, pivot_idx=0, temp_right_idx=2)

        #then
        self.assertEqual(result, 0)
        
    def test_swap(self):
        # given
        arr = [3,4,2,8,5,9,0,1,6,7]

        # when
        quick.swap(arr, i1 = 1, i2 = 7)

        #then
        self.assertEqual(arr, [3,1,2,8,5,9,0,4,6,7])
        
    def test_is_crossed(self):
        # when
        result1 = quick.is_crossed(1, 8)
        result2 = quick.is_crossed(4, 3)

        #then
        self.assertFalse(result1)
        self.assertTrue(result2)
        
    def test_sort(self):
      # given
      arr = [3,4,2,8,5,9,0,1,6,7]
            
      # when
      quick.sort(arr)
    
      # then
      self.assertEqual(arr, [0,1,2,3,4,5,6,7,8,9])


if __name__ == '__main__':
    unittest.main()