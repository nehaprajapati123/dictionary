#  interview question:-
list1=[[1,2,3],[4,5,6]]
list3=[]

for j in list1[0]:
    list2=[]
    for k in list1[1]:
        list2.append(j)
        list2.append(k)
    list3.append(list2)
print(list3)










# list1=[1,2,[3,4,5,6],7,[8,9],10]
# i=0
# sum=0
# while i<len(list1):
#     if type(list1[i]) != list:
#         sum=sum+(list1[i])
#     else:
#         j=0
#         while j<len(list1[i]):
#             sum=sum+(list1[i][j])
#             j=j+1
#     i=i+1
# print(sum)
# list1=[1,2,3,[3,4,5],2,4,5,[4,5,6],[6,4,5]]
# i=0
# sum=0
# while i<len(list1):
#     if type (list1[i])!=list:
#         sum=sum+(list1[i])
#     else:
#         j=0
#         while j<len(list1[i]):
#             sum=sum+(list1[i][j])
#             j=j+1
#     i=i+1
# print(sum)
    

# a="nEhapraJapatI"
# i=0
# c1=0
# c2=0
# while i<len(a):
#     if a[i]>="A" and a[i]<="Z":
#         c1=c1+1
#     elif a[i]>="a" and a[i]<="z":
#         c2=c2+1
#     else:
#         print("you went somwthing wrong")
#     i=i+1
# print(c1,"upper case")
# print(c2,"lower case")