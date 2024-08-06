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

def solution(food_times:list, k):
    total_times = sum(food_times)
    if total_times <= k:
        return -1
    max_num = max(food_times)
    result_arr:list = [[] * max_num for _ in range(max_num)]
    for i, v in enumerate(food_times):
        for j in range(0, v):
            result_arr[j].append(i)
    return sum(result_arr, [])[k] + 1

if __name__ == '__main__':
    unittest.main()