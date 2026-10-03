from collections import deque

a = int(input("Enter capacity of jug 1: "))
b = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

queue = deque([((0, 0), [])])
visited = {(0, 0)}

while queue:
    (x, y), path = queue.popleft()

    if x == target or y == target:
        print("\nSolution:")
        for state in path + [(x, y)]:
            print(state)
        break

    states = [
        (a, y), (x, b),
        (0, y), (x, 0)
    ]

    p = min(x, b - y)
    states.append((x - p, y + p))

    p = min(y, a - x)
    states.append((x + p, y - p))

    for state in states:
        if state not in visited:
            visited.add(state)
            queue.append((state, path + [(x, y)]))
else:
    print("No solution")
    




