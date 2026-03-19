l = input()
result = ''
for i in range(0, len(l)):
    if i + 1 == len(l):
        result += l[i]
    elif l[i] == ' ':
        if i == 0:
            continue
        result += l[i-1]
print(result)