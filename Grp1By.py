str = "111222311"
l1 = list(str)
# (1,1) (3,2) (1,3) (2,1)  =>  (count, val)

val = l1[0]
cnt = 1
for i in range(1, len(str)):
    if l1[i] == val:
       cnt = cnt + 1
       if i == len(str)-1 :
           print(cnt, val )

    else:
        print(cnt, val)
        val = l1[i]
        cnt = 1



