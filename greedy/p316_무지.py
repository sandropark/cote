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
    if sum(food_times) <= k:
        return -1
    max_num = max(food_times)
    result_arr:list = [[] for _ in range(max_num)]
    for i, v in enumerate(food_times):
        result_arr[i] = [i] * v
    result_arr = transposition(result_arr)
    return sum(result_arr, [])[k] + 1

def transposition(arr:list) -> list:
    transformed_list =[[] for _ in arr]
    for inner in arr:
        for j, e in enumerate(inner):
            transformed_list[j].append(e)
    return transformed_list

if __name__ == '__main__':
    unittest.main()
