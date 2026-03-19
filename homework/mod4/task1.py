def task1(str_numbers: str) -> None:
    m = list(map(int, str_numbers.split()))
    only_different = len(set(m))
    if only_different == 1:
        print("Все числа равны")
    if len(m) == only_different:
        print("Все числа разные") #не elif для обработки случая, когда всего 1 число
    else:
        print("Есть равные и неравные числа")
