# for i in range(1,20):
#     print(i)

big = []
for i in range(1,1000000):
    big.append(i)
print("sum: " +str(sum(big))+ "\nmin:" +str(min(big))+ "\nmax:" +str(max(big)))

for j in range(1,20,2):
    print(j)

for k in range(3,30,3):
    print(k)

for v in range(1,20):
    aa = v**3
    print(aa)

list = [m**3 for m in range(1,20)]
print(list)
