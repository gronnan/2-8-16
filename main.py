print("Выберите систему счистления в которую хотите перекодировать число\n")

number_systems = ["binary","octal","hexadecimal"]

print(number_systems[0], "= 1")
print(number_systems[1], "= 2")
print(number_systems[2], "= 3\n")

print("Выберите систему:",end='',sep='')
x = int(input())

print("Введите число:", end='',sep='')
if x == 1:
    y = int(input())
    print(bin(y), "- ваше число в двоичной системе счисления")
elif x == 2:
    y = int(input())
    print(oct(y), "- ваше число в восьмеричной системе счисления")
elif x == 3:
    y = int(input())
    print(hex(y), "- - ваше число в шестнадцатеричной системе счисления")
else:
    print("error")