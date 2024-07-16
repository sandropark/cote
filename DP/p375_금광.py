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
    for col_idx in range(n):
        for row_idx in range(m):
            find_max(arr, temp_arr, col_idx, row_idx)
    return max(temp_arr[n-1])

# 합이 가장 큰 조합을 찾아서 temp_arr를 갱신
def find_max(arr, temp_arr, col_idx, row_idx):
    # 이전 결과 찾기
    pre_col_idx = col_idx - 1
    pre_row_idx = row_idx - 1
    next_row_idx = row_idx + 1
    
    if pre_col_idx >= 0:
        pass
    
    
    if temp_arr[col_idx][row_idx] == 0:
        temp_arr[col_idx][row_idx] = arr[col_idx][row_idx]
        return



if __name__ == '__main__':
    unittest.main()