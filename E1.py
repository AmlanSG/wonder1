inp = input('Enter Fahrenheit Temperature:')
inp1 = input('Enter Divisor:')
try:
    fahr = float(inp)
    print "1st Exception"
    cel = (fahr - 32.0) * 5.0 / inp1
    print "2nd Exception"
    print(cel)
except ValueError:
    print('Please enter a number')

except ZeroDivisionError:
    print('Please enter a NON ZERO number')