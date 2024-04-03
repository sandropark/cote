def greedy_1():
    arr = [2,4,5,4,6]
    m = 8
    k = 3

    arr.sort(reverse=True)  # 내림차순 정렬 [6,5,4,4,2]

    result = 0
    iteration = 0
    first = True
    for _ in range(m):
        if iteration == k:  # 반복횟수 k에 도달하면 두번째로 큰 수를 더한다.
            iteration = 0
            first = False
        if first:
            result += arr[0]
            iteration += 1
        else:
            result += arr[1]
            first = True    # 다시 첫번째로 큰 수를 더하기 위해 True로 변경

    assert result == 46

greedy_1()

# 반복문 안 쓰는 방법
def greedy_2():
    arr = [2,4,5,4,6]
    m = 8
    k = 3

    arr.sort(reverse=True)  # 내림차순 정렬 [6,5,4,4,2]

    first = arr[0]
    second = arr[1]
    first_times = m//k*k
    second_times = m - first_times
    result = first*first_times + second*second_times
    
    assert result == 46

greedy_2()