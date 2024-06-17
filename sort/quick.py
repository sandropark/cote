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

def sort(arr:list, end:int, start:int=0):
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
        sort(arr, start=start, end=end)