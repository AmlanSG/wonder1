K = int(input("Number of Member per room:"))


rooms = []
n = input("enter length")
for i in range(0, int(n)):
    u=int(input("enter value"))
    rooms.append(u)
print (rooms)
print(len(rooms))

for j in range(0,int (n)):
    if rooms.count(rooms[j]) < 2:
        print("Captain", rooms[j] )
