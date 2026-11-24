inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [0, 0, 0, 1]

w1 = 0
w2 = 0
bias = 0
learning_rate = 1

for epoch in range(5):
    for i in range(4):
        x1 = inputs[i][0]
        x2 = inputs[i][1]

        total = x1 * w1 + x2 * w2 + bias

        if total >= 1:
            prediction = 1
        else:
            prediction = 0

        error = outputs[i] - prediction

        w1 = w1 + learning_rate * error * x1
        w2 = w2 + learning_rate * error * x2
        bias = bias + learning_rate * error

    print("Iteration:", epoch + 1)
    print("Weights:", w1, w2, "Bias:", bias)

print("\nTesting AND Gate:")
for i in range(4):
    total = inputs[i][0] * w1 + inputs[i][1] * w2 + bias

    if total >= 1:
        result = 1
    else:
        result = 0

    print(inputs[i], "=", result)
