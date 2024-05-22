# 이코테 341페이지 - 연구소

wall_limit = 3
n, m = list(map(int, list(input())))
        
my_map = []
for i in range(n):
    my_map.append(list(map(int, list(input()))))

#[[2, 0, 0, 0, 1, 1, 0], 
# [0, 0, 1, 0, 1, 2, 0], 
# [0, 1, 1, 0, 1, 0, 0], 
# [0, 1, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 1, 1], 
# [0, 1, 0, 0, 0, 0, 0], 
# [0, 1, 0, 0, 0, 0, 0]]

result = 0

temp_map = [[0] * m for _ in range(n)]

# 좌, 상, 우, 하
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):
    for i in range(4):
        spread(x + dx[i], y + dy[i])

def spread(x, y):
    if _can_spread(x, y):
        temp_map[x][y] = 2
        virus(x, y)

def _can_spread(x, y) -> bool:
    return _is_location_valid(x, y) and _is_empty(x, y)

def _is_location_valid(x, y) -> bool:
    return x >= 0 and x < n and y >= 0 and y < m

def _is_empty(x, y):
    return temp_map[x][y] == 0

def get_score() -> int:
    score = 0
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                score += 1
    return score
    
def simulate():
    # 임시 맵에 데이터 복사
    for i in range(n):
        for j in range(m):
            temp_map[i][j] = my_map[i][j]
    # 임시 맵의 바이러스 전파
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 2:
                virus(i, j)
    update_score()
    
def update_score():
    global result
    result = max(result, get_score())

def make_wall(wall_count : int):
    for i in range(n):
        for j in range(m):
            if my_map[i][j] == 0:
                my_map[i][j] = 1
                wall_count += 1
                dfs(wall_count)
                my_map[i][j] = 0
                wall_count -= 1

def dfs(wall_count : int = 0):
    if wall_count == wall_limit:
        simulate()
        return
    make_wall(wall_count)

dfs()
print(result)


# 1. 그래프를 순회하면서 하나씩 벽을 세운다.
# 2. 벽이 3개 세워졌다면 임시 맵에 현재 맵을 복사한다.
# 3. 임시 맵의 바이러스를 퍼트린다.
# 4. 임시 맵의 빈 공간을 세고, 현재 최대 빈 공간을 업데이트한다.
# 5. 벽을 하나 허문다. 
# 6. 1~5를 반복한다.
