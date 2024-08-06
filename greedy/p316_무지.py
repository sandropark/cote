import unittest

class Test(unittest.TestCase):
    def test(self):
        # given
        food_times = [3, 1, 2] # 0,1,2,0,2,0
        k = 5

        # when
        result = solution(food_times, k)

        # then
        self.assertEqual(result, 1)

    def test_k가_음식의_총_합_이상인_경우(self):
        # given
        food_times = [1]
        k = 1

        # when
        result = solution(food_times, k)

        # then
        self.assertEqual(result, -1)

def solution(food_times, k):
    total_times = sum(food_times)
    if total_times <= k:
        return -1
    result_arr = []
    for i in range(0, total_times+1):
        value = food_times[i % 3]
        if value:
            food_times[i % 3] = value-1
            result_arr.append(i % 3)
    return result_arr[k] + 1
            
            

if __name__ == '__main__':
    unittest.main()