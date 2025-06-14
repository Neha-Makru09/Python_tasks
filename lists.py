l=[1,2,67,34,3,4,5,4,6,8]
print(l) 
print(sum(l))
print(min(l), max(l))
print(l[-1])
l[0]=48 
print(len(l))

y=['Abel', 'Lily','Ruby']
l.append(y)
print(l, len(l))

print(l[0:4:2])
print(l[::2])
print(l[10][1])

print("\nPrinting the elements using loops")

print("\nWe are making use of the for loop here")

for i in y: print (i)

print("\nWe are making use of the while loop here")
i=0
while (i<len(y)): 
    print(y[i])
    i+=1 
