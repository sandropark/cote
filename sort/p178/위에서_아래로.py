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
        for i in range(1, len(arr)):
            temp = arr[i]
            # 가장 앞 요소보다 작으면, 가장 앞으로 보낸다.
            if temp > arr[0]:
                arr.insert(0, arr.pop(i))
            else:
                # 0부터 i까지 순회하면서 temp보다 큰 값이 있는 경우 그 앞에 넣는다.
                for j in range(1, i):
                    if temp > arr[j]:
                        arr.insert(j, arr.pop(i))
                        break
        return arr

    def quick_sort(arr:list, start:int=0, end:int=-10) -> list:
        if end == -10: end = len(arr)-1
        pivot_idx = start
        left_idx = start+1
        right_idx = end
        if start >= end: return
        
        # left 피벗보다 작은 수를 찾기
        while arr[left_idx] > arr[pivot_idx] and left_idx < end:
            left_idx+=1
        # right 피벗보다 큰 수를 찾기
        while arr[right_idx] < arr[pivot_idx] and right_idx > start:
            right_idx-=1
            
        if Sort.__is_crossed__(left_idx, right_idx):
            Sort.__swap__(arr, pivot_idx, right_idx)
            # 왼쪽
            Sort.quick_sort(arr, end=right_idx-1)
            # 오른쪽
            Sort.quick_sort(arr, start=right_idx+1, end=end)
        else :
            Sort.__swap__(arr, left_idx, right_idx)
            Sort.quick_sort(arr, start=start, end=end)
        
        return arr

    def __swap__(arr:list, i1:int, i2:int):
        arr[i1], arr[i2] = arr[i2], arr[i1]
        
    def __is_crossed__(left_idx:int, right_idx:int) -> bool:
        return left_idx >= right_idx
    
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