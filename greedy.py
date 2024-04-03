class 큰수의법칙:
    @staticmethod
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
    @staticmethod
    def greedy_2():
        arr = [2,4,5,4,6]
        m = 8
        k = 3

        arr.sort(reverse=True)  # 내림차순 정렬 [6,5,4,4,2]

        first = arr[0]
        second = arr[1]
        # first_times = m//k*k
        first_times = m//(k+1)*k + m%(k+1)
        assert first_times == 6
        second_times = m - first_times
        assert second_times == 2
        result = first*first_times + second*second_times
        assert result == 46

    greedy_2()

    @staticmethod
    def greedy_3():
        arr = [2,4,5,4,6]
        m = 8
        k = 4

        arr.sort(reverse=True)  # 내림차순 정렬 [6,5,4,4,2]

        first = arr[0]
        second = arr[1]
        first_times = m//(k+1)*k + m%(k+1)  
        # m에 k+1을 나눈 몫에 k를 곱하고 m에 k+1을 나눈 나머지를 더한다.
        # m에 k+1을 나눈 몫 = 1 * k = 4
        # m에 k+1을 나눈 나머지 = 8 % 5 = 3
        # 둘을 더한 값 = 7 이게 가장 큰 수를 곱하는 수
        assert first_times == 7
        second_times = m - first_times
        assert second_times == 1
        result = first*first_times + second*second_times
        assert result == 47

큰수의법칙().greedy_1()
큰수의법칙().greedy_2()
큰수의법칙().greedy_3()

class 모험가길드:
    @staticmethod
    def case1():
        n = 5
        arr = [2,3,1,2,2]

        arr.sort(reverse=True)

        group = 0
        people = 0
        for x in arr:
            if people == 0:
                people = x
            
            people-=1

            if people == 0:
                group += 1

        assert group == 2

모험가길드().case1()