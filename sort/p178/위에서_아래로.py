class Sort:
    def select_sort(arr:list) -> list:
        # 배열을 순회
        for first_idx in range(len(arr)):
            max_idx = first_idx
            # 처음 인덱스 다음부터 순회하면서 제일 큰 값을 찾는다.
            for j in range(first_idx + 1, len(arr)):
                if (arr[j] >= arr[max_idx]):
                    max_idx = j

            # 제일 큰 값을 현재 배열의 가장 앞으로 이동한다.
            arr[first_idx], arr[max_idx] = arr[max_idx], arr[first_idx]
        return arr

    def insertion_sort(arr:list) -> list:
        pass

    def quick_sort(arr:list) -> list:
        pass

    def count_sort(arr:list) -> list:
        # 배열 초기화
        new_list : list = [0] * (max(arr)+1)

        # 배열 순회하면서 카운팅
        for item in arr:
            new_list[item] += 1

        # 카운팅한 배열을 거꾸로 순회하면서 실제 값으로 변경
        return [item 
                for i in range(len(new_list) - 1, -1, -1)
                if new_list[i] != 0 
                for item in [i] * new_list[i]]