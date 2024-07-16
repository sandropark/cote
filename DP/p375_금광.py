import unittest

class Test(unittest.TestCase):
    def test(self):
        # given
        arr = [[1,2,0], [3,1,6], [3,4,4], [2,1,7]]

        # when
        result = solution(arr, 3, 4)

        # then
        self.assertEqual(result, 19)


def solution(arr:list, n:int, m:int) -> int:
    temp_arr = [[0] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            find_max(arr, temp_arr, i, j)
    return max(temp_arr[n-1])

# 합이 가장 큰 조합을 찾아서 temp_arr를 갱신
def find_max(arr, temp_arr, i, j):
    pass



# 바로 위 아래 대각선으로만 이동이 가능하다.
# 현재 (1, 0) = 3
# (0, 0), (0, 1)

# (1, 1) = (0, 0), (0, 1), (0, 2)

# pre_col_idx = i - 1


# temp_e = temp_arr[i][j]
# if temp_e == 0:
#     temp_arr[i][j] = arr[i][j]
        


if __name__ == '__main__':
    unittest.main()