import unittest

class BinarySearch(unittest.TestCase):
    def test_1(self):
        # given
        arr = [0,1,2,3,4,5,6,7,8,9]
      
        for i in arr:
            # when
            result = search(arr, i, 0, len(arr)-1)
            
            # then
            self.assertEqual(result, i)
    
    def test_2(self):
        # given
        arr = [0,1,2,3,4,5,6,7,8,9]
    
        # when
        result = search(arr, 10, 0, len(arr)-1)
        
        # then
        self.assertEqual(result, None)
    
    def test_3(self):
        # given
        arr = [0,1,2,3,4,5,6,7,8,9]
    
        # when
        result = search(arr, -1, 0, len(arr)-1)
        
        # then
        self.assertEqual(result, None)

def search(arr:list, target:int, start_idx:int, end_idx:int) -> int:
    if start_idx > end_idx:
        return
    center_idx = (end_idx-start_idx) // 2 + start_idx
    center_element = arr[center_idx]
    if center_element == target:
        return  center_idx
    elif target > center_element:
        return search(arr, target, center_idx+1, end_idx)    
    elif target < center_element:
        return search(arr, target, start_idx, center_idx-1)



if __name__ == '__main__':
    unittest.main()