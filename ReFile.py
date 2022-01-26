cntr = 0
try :
    f = open("F:\\pythonall1\\TEST.txt","r")
    print type(f)
    for line in f:
        print line
        line = line.rstrip()
        print type(line)
        print (line)
        if line.find("Deb") > 0:
            cntr = cntr +1

    print cntr
except IOError:
    print "No Such File"

