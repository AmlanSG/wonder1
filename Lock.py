import itertools

def guessables(num):
    guesses = []
    for p in itertools.permutations(xrange(10),num):
        if p[0] != 0:
            guesses.append(''.join(map(str, p)))
    return guesses

print(guessables(4))

print([str(a)+str(b)+str(c)+str(d) for a in range(1,10) for b in range(0,10) if a!=b for c in range(0,10) if b!=c and a!=c for d in range(0,10) if c!=d and d!=b and d!=a])

