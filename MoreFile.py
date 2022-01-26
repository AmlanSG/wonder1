try :
    f = open("F:\\pythonall1\\TEST4.txt","a")
    print type(f)
    f.write("\n")
    f.write("This is Debasis")
    #f.next()
    f.write("\n")
    f.writelines("I am Debasis")



except IOError:
    print "No Such File"