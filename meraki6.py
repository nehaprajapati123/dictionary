dic1={
    "ball":"red",
    "ball":4,
    "wicket":8,
    "ball":"green",
    "bat":3
    }
print(dic1)

dic2={}
for k in dic1:
    if k not in dic2:
        dic2[k]=dic1[k]
print(dic2)

     
    