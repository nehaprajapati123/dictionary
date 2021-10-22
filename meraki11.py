dic = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
a=0
b=0
c=0
list=[]
for i in dic:
    if dic[i]>a:
        c=b
        b=a
        a=dic[i]
list.append(c)
list.append(b)
list.append(a)
print(list)
    
    

