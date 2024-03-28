'''n = int(input())
if(n/2 != 0):
    print("Weird")
else:
    if(n in range(2, 6)):
        print("Not Weird")
    elif(n in range(6 , 21)):
        print("Weird")
    elif(n > 20):
        print("Not Weird")'''

for i in range(6):
    for j in range(i):
        j+=1
        print(i,end='')
    print("\n")
    #i+=1
for i in range(6):
    for j in range(i):
        print(j+1,end='')
    print("\n")
    i+=1