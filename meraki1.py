dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
for k in dic1:
    if k in  dic2:
        sum=dic1[k]+dic2[k]
        dic4[k]=sum
    else:
        for k in (dic1,dic2,dic3):
            print(k)
    
print(dic4)
        
