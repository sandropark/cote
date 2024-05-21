# 이코테 339페이지 15번 특정 거리의 도시 찾기 - BFS

# 어떤 나라에는 1 ~ N번까지의 도시와 M개의 단방향 도로가 존재합니다. 모든 도로의 거리는 1입니다.이때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서,최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하세요.또한 출발 도시 X에서 출발 도시 X로가는 최단 거리는 항상 0이라고 가정합니다. 1 예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 합시다. 이때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시뿐입니다. 2번과 3번 도시의 경우,최단 거리가 1이기 때문에 출력하지 않습니다.

# 1. 그래프 만들기 - 인접 행렬, 인접 리스트

from typing import Deque


vertex, edge, target_count, start_vertex = 4,4,2,1

raw_graph = [(1,2), (1,3), (2,3), (2,4)]

graph = {1:[2, 3], 2:[3, 4]}
visited = [0] * (vertex + 1)
result = []
queue = Deque()

def bfs(start_vertex):
    queue.append(start_vertex)
    visited[start_vertex] = 1
    for temp in graph[start_vertex]:
        queue.append(temp)

    while len(queue):
        poped_vertex = queue.popleft()
        if not visited[poped_vertex]:
            visited[poped_vertex] = 1
            for temp in graph[poped_vertex]:
                queue.append(temp)
    
        
bfs(start_vertex)


