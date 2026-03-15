str = input()
result = ''
ignored = '-() '
for i in range(0, len(str)):
    if ignored.find(str[i]) == -1:
        result += str[i]
print(result)