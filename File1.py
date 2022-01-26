try :
    f1 = open("F:\\Python\\pythonall1\\F1.txt","r")
    f2 = open("F:\\Python\\pythonall1\\F2.txt","r")
    Of = open("F:\\Python\\pythonall1\\F3.txt", "w")
    k1 = str (f1.readlines())
    k2 = str (f2.readlines())
    a1 = k1.split(",")
    a2 = k2.split(",")
    cnt1 = len(a1)
    cnt2 = len(a2)
    print (cnt1)
    for i in range (0,cnt1):
        #print "\n"
        #print a2[i]
        if a1[i] != a2[i] :
               print (a2[i])
               Of.write(a2[i])



    f1.close()
    f1.close()
    Of.close()
except IOError:
    print ("Error Occured")