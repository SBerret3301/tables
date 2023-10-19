tab1 = []
tab2 = []
tab3 = []
x = int(input("enter the size of the both tables : "))
for i in range (0,x) :
    a = int(input("enter a numbers for the first table : "))
    tab1.append(a)
for i in range (0,x) :
    b = int(input("enter a numbers for the second table : "))
    tab2.append(b) 
for i in range (0,x) :
    c = tab1[i] + tab2[i]
    tab3.append(c)
print("the sum of the both table is : ",tab3)