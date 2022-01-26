txt = 'Amlan Neha Dippanjan Rashmi'
words = txt.split()
print (type(words)) # list data type
print (words)
t = list()
print (type(t))
for dii in words:
    t.append((len(dii), dii))
print (t)
t.sort(reverse = True)
print (t)
res = list()
for neha, reshmi in t:
    res.append(reshmi)

print(res)
