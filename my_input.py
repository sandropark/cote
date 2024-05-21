vertex, edge, target, start = map(int, input().split())

graph = [0] * (vertex + 1)

my_input = input()
while(my_input):
    f, t = map(int, my_input.split())
    graph[f] = t
    my_input = input()

print(vertex, edge, target, start)
print(graph)