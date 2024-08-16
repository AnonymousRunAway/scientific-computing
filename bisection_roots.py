def bisection_roots(x: float, n: float, epsilon: float = 1e-7, max_iterations: int = 100):
    f = lambda y: y**n - x
    low = 0
    high = x if x > 1 else 1
    mid = 0
    while max_iterations:
        mid = low + (high - low)/2
        if abs(f(mid)) < epsilon:
            return mid
        elif f(mid) < 0:
            low = mid
        else: high = mid
        max_iterations -= 1
    return mid

print(bisection_roots(8.000, 3))