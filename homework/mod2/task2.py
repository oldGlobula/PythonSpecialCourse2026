# from math import sqrt - considered "Дополнительные библиотеки"? - decided they are. For sureness
SQRT_2 = 1.4142135623730950488016887242 # instead of importing sqrt
def str2(number):
    return format(number, '.2f')

a = float(input())
result = f"{str2(a*4)}, {str2(a*a)}, {str2(SQRT_2*a)}"
print(result)