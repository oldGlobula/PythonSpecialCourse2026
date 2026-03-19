def task3(a: int, b: int) -> int:
    max = a if a > b else b
    min = a if a < b else b
    if max % min == 0:
        return min
    return task3(min, max % min)