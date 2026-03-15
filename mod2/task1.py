input_string = input()
i = input_string.find(',')

a = int(input_string[:i])
b = int(input_string[i+2:])
print(a%b)
