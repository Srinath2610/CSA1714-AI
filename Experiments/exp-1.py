from collections import deque

start = list(map(int, input("Enter initial state: ").split()))
goal = list(map(int, input("Enter goal state: ").split()))

queue = deque([(start, [])])
visited = {tuple(start)}

while queue:
    state, path = queue.popleft()

    if state == goal:
        path.append(state)

        for i, s in enumerate(path[1:], 1):
            if s == goal:
                print("\nGoal State:")
            else:
                print("\nStep", i, ":")
            print(s[:3])
            print(s[3:6])
            print(s[6:])
        break

    zero = state.index(0)

    moves = []
    if zero >= 3:
        moves.append(zero - 3)
    if zero < 6:
        moves.append(zero + 3)
    if zero % 3 != 0:
        moves.append(zero - 1)
    if zero % 3 != 2:
        moves.append(zero + 1)

    for move in moves:
        new = state.copy()
        new[zero], new[move] = new[move], new[zero]

        if tuple(new) not in visited:
            visited.add(tuple(new))
            queue.append((new, path + [state]))
