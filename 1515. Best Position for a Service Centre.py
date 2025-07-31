# https://leetcode.com/problems/best-position-for-a-service-centre
# Q: Find (X,Y) that minimize sum of Euclidean distance to given points
#
# Gradient descent
# Cost function: sum(sqrt((x_i - X)^2 + (y_i - Y)^2))
# Gradient function: shown below, calculated using partial derivatives


def getMinDistSum(positions: list[list[int]]) -> float:
    n = len(positions)

    # haven't learnt how to pick these values yet, just tried random ones until it worked
    eps = 1e-13
    iters = 1000000
    alpha = 5

    def cost_function(X, Y):
        return sum(((X - x_i) ** 2 + (Y - y_i) ** 2) ** 0.5 for x_i, y_i in positions)

    def gradient_function(X, Y):
        dx = dy = 0
        for x_i, y_i in positions:
            dx += ((X - x_i) ** 2 + (Y - y_i) ** 2 + eps) ** -0.5 * (X - x_i)
            dy += ((X - x_i) ** 2 + (Y - y_i) ** 2 + eps) ** -0.5 * (Y - y_i)
        return dx, dy

    # gradient descent, start somewhere in the middle of the points
    X = sum(x for x, y in positions) / n
    Y = sum(y for x, y in positions) / n
    for _ in range(iters):
        dx, dy = gradient_function(X, Y)
        X, Y = X - alpha * dx, Y - alpha * dy
        if dx * dx + dy * dy < eps:  # close enough
            break
        alpha *= 0.995

    return cost_function(X, Y)


print(getMinDistSum(positions=[[0, 1], [1, 0], [1, 2], [2, 1]]))
print(getMinDistSum(positions=[[1, 1], [3, 3]]))
print(getMinDistSum(positions=[[1, 1]]))
print(getMinDistSum(positions=[[58, 32], [41, 21]]))
