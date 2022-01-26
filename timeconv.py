def sec2hoursmin(seconds):
    a=str(seconds//3600)
    b=str((seconds%3600)//60)
    c=str((seconds%3600)%60)
    d=["{} hours {} mins {} seconds".format(a, b, c)]
    return d



x = int( input("Enter Secs:"))

print(sec2hoursmin(x))


