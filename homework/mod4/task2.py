def task2(a, n: int) -> typeof(a):
    if n == 0:
        return 1
    if (n % 2) == 0:
        return task2(a, n // 2)*task2(a, n // 2)
    else:
        return a * task2(a, n - 1)
