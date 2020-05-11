column = int(input())
row = int(input())
edges = [1, 8]

if (edges[0] < column < edges[1]) and (edges[0] < row < edges[1]):
    print(8)
elif column in edges and row in edges:
    print(3)
else:
    print(5)