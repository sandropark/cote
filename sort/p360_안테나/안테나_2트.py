n = int(input())
arr : list = list(map(int, input().split()))

avg = sum(arr)/len(arr)

sorted_list = sorted(arr)

for i in range(len(sorted_list)-1):
    temp = sorted_list[i]
    if temp == avg:
        print(temp)
    if temp < avg < sorted_list[i+1]:
        a = avg - temp
        b = sorted_list[i+1] - avg
        print(temp if a < b else sorted_list[i+1])