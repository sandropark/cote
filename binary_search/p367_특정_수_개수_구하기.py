import unittest

class Test(unittest.TestCase):
    def test(self):
        # given
        n, x = 7, 2
        arr = [1,1,2,2,2,2,3]

        # when
        result = search(arr, x, 0, n-1)

        # then
        self.assertEqual(result, 4)
    def test_2(self):
        # given
        n, x = 7, 4
        arr = [1,1,2,2,2,2,3]

        # when
        result = search(arr, x, 0, n-1)

        # then
        self.assertEqual(result, -1)

def search(arr:list, target:int, start_idx:int, end_idx:int)->int:
    if start_idx > end_idx:
        return -1
    center_idx = (end_idx-start_idx) // 2 + start_idx
    center_element = arr[center_idx]
    if center_element == target:
        return  count(arr, center_idx)
    elif target > center_element:
        return search(arr, target, center_idx+1, end_idx)    
    elif target < center_element:
        return search(arr, target, start_idx, center_idx-1)

def count(arr:list, target_idx:int) -> int:
    count = 1
    up = target_idx+1
    down = target_idx-1
    while arr[up] == arr[target_idx]:
        count +=1
        up+=1
    while arr[down] == arr[target_idx]:
        count +=1
        down-=1
    return count

if __name__ == '__main__':
    unittest.main()