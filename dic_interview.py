x={"my name":["a","b","c"],"age of student":[21,22,23],
"present in campus":["number","of","student","in","campus",160]}

dic={}
a=" "
for i in x:
    temp=" "
    for j in i:
        if j==a:
            pass
        else:
            temp=temp+j
    string=""
    sum=0
    for k in x[i]:
        temp2=str(k)
        if temp2!=k:
            sum=sum+k
            string=str(sum)
           
        else:

            string=string+k
            
    dic[temp]=string
print(dic)

    
