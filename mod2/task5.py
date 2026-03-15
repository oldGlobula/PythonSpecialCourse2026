name = input()
s = name[::-1]
while len(s) > 1:
    i = s.find('.')
    if i == -1:
        print(s[::-1])
        break
    subs = s[:i]
    print(subs[::-1])
    s = s[i+1:]
