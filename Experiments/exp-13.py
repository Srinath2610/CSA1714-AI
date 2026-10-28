
def minimax(scores, is_max):
    if len(scores) == 1:
        return scores[0]

    next_scores = []

    for i in range(0, len(scores), 2):
        first = scores[i]
        second = scores[i + 1]

        if is_max:
            best = max(first, second)
            print("MAX chooses:", best)
        else:
            best = min(first, second)
            print("MIN chooses:", best)

        next_scores.append(best)

    return minimax(next_scores, not is_max)


print("MINIMAX ALGORITHM")
scores = [3, 5, 2, 9, 12, 5, 23, 23]

print("Possible scores:", scores)

result = minimax(scores, True)

print("Best score:", result)

