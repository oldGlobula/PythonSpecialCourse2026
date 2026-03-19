a = 0
s = input()
try :
	a = int(s)
except :
    print("Неверный ввод")
    exit()

if a <= 0:
    print("Неверный ввод")
    exit()

a_1 = a
a_2 = a
s_2 = ''
s_8 = ''
s_16 = ''
while a > 0:
    s_2 += str(a % 2)
    a //= 2

while a_1 > 0:
    s_8 += str(a_1 % 8)
    a_1 //= 8

while a_2 > 0:
    s_16 += str(a_2 % 16)
    a_2 //= 16
print(f'{s_2[::-1]}, {s_8[::-1]}, {s_16[::-1]}')