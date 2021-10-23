dic={}
n=int(input("enter number of element  "))
for k in range(1,n+1):
    element=int(input("enter your number "))
    dic[k]=element
    k=k+1
for i in dic:
    for j in dic:
        if dic[i]<dic[j]:
            a=dic[i]
            dic[i]=dic[j]
            dic[j]=a
print(dic)