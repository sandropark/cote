arr = [3,4,2,8,5,9,0,1,6,7]

# 피벗 선택 : 가장 처음 원소
# 1. 왼쪽 포인터는 오른쪽으로 가면서 피벗보다 큰 원소를 찾으면 스톱
# 2. 오른쪽 포인터는 왼쪽으로 가면서 피벗보다 작은 원소를 찾으면 스톱
# 3. 두 값을 스왑
# 4. 두 포인터가 엇갈린다면 오른쪽 포인터가 찾은 값과 피벗을 스왑
# 5. 피벗을 기준으로 리스트를 반으로 분할
# 각 리스트에 대해 리스트의 원소가 1개남을 때까지 1~5까지 반복
    
def find_left_idx(arr:list, pivot_idx:int, temp_left_idx:int, end:int) -> int:
    while arr[temp_left_idx] < arr[pivot_idx] and temp_left_idx < end:
        temp_left_idx+=1
    return temp_left_idx

def find_right_idx(arr:list, pivot_idx:int, temp_right_idx:int, start:int=0) -> int:
    while arr[temp_right_idx] >= arr[pivot_idx] and temp_right_idx > start:
        temp_right_idx-=1
    return temp_right_idx

def swap(arr:list, i1:int, i2:int):
    arr[i1], arr[i2] = arr[i2], arr[i1]
    
def is_crossed(left_idx:int, right_idx:int) -> bool:
    return left_idx > right_idx

def sort(arr:list, start:int=0, end:int=len(arr)-1):
    pivot_idx = start
    left_idx = start+1
    right_idx = end
    if start >= end: return
    
    left_idx = find_left_idx(arr, pivot_idx, left_idx, end)
    right_idx = find_right_idx(arr, pivot_idx, right_idx, start)
    
    if right_idx == start: return
    
    if is_crossed(left_idx, right_idx):
        swap(arr, pivot_idx, right_idx)
        # 왼쪽
        sort(arr, end=right_idx-1)
        # 오른쪽
        sort(arr, start=right_idx+1, end=len(arr)-1)
    else :
        swap(arr, left_idx, right_idx)
        sort(arr, start, end)