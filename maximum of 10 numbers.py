x=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input(" "))
    x.append(b)
x.sort()
print("Largest element is:",x[n-1])
