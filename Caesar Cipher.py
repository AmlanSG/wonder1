#cIPHER

str = input("Enter String:")
lstr = list(str)
CiNum = int(input("Enter Cipher Num:"))
for i in range (len(lstr)):
    asciival = ord(lstr[i]) + CiNum
    if asciival > 122:
        rndoff = asciival -122
        asciival = 97 + rndoff -1
    lstr[i]= chr(asciival)

svar = "".join(lstr)
print(svar)