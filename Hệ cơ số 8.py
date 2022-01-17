s = input()
binary = ['000','001','010','011','100','101','110','111']
while len(s) % 3 != 0:
    s = '0' + s
tmp = ""
number = ""
for i in range(len(s) - 1,-1,-1):
    if len(tmp) < 3:
        tmp = s[i] + tmp
    if len(tmp) == 3:
        for j in range(len(binary)):
            if tmp == binary[j]:
                number = str(j) + number
        tmp = ""
print(int(number))