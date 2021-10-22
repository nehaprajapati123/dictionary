list1=["one","two","three","four","five"]
list2=[1,2,3,4,5]
# {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}  output

dic={}
for k in list1:
    for j in list2:
        dic[k]=j
        list2.remove(j)
        break
print(dic)