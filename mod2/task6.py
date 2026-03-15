str = input()
zeros = 0
ones = 0
for i in str:
    if i == '0':
        zeros += 1
    elif i == '1':
        ones += 1

print('yes' if zeros == ones else 'no')