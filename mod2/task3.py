s = input()

i = 0
while s[i] != ' ':
    i += 1

j = i + 1
while s[j] != ' ':
    j += 1

a = int(s[:i])
b = int(s[i+1:j])
c = int(s[j+1:])

print(a + b + c - min(a, b, c) - max(a, b, c))