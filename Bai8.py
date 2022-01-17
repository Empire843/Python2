# text = "ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam! " \
#        "vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11."
text = ""
while True:
    try:
        str = input()
        text += str + " "
    except EOFError:
        break
text = text.lower()
para = text.replace('.','\n')
para = para.replace('!', '\n')
para = para.replace('?','\n')
s = para.split("\n")

text = ""
for i in s:
       str = i.split()
       str1 = " ".join(str)
       str1 = str1.capitalize()
       text+=str1+'\n'
       # print(str1)
print(text.strip())