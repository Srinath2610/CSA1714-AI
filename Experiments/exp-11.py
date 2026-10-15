
colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

color = {}

def safe(node, c):
    for neighbor in graph[node]:
        if neighbor in color and color[neighbor] == c:
            return False
    return True

def solve(node):
    if node == len(graph):
        return True

    region = list(graph.keys())[node]

    for c in colors:
        if safe(region, c):
            color[region] = c

            if solve(node + 1):
                return True

            del color[region]

    return False

if solve(0):
    print("Map Coloring Solution:")
    for region in color:
        print(region, ":", color[region])
else:
    print("No solution")
