# a1=int(input("enter your  angle"))
# a2=int(input("enter your angle"))
# a3=int(input("enter your  angle"))
# if a1+a2+a3==180:
#     print("the triangle is possible")
# else:
#     print("not possible")  que1

# n=int(input("enter your number"))

# if n%3==0 and n%5==0:
#     print("fizz-buzz")
# elif n%3==0:
#     print("fizz")
# elif n%5==0:
#     print("buzz")
# else:
#     print("buzz-fizz")   que2

# num1=int(input("enter your 1st number"))
# num2=int(input("enter your 2st number"))
# num3=int(input("enter your 3st number"))


# if num1>num2 and num1>num3:
#     if num2>num3:
#         print(num1,"is greater",num2,"is medium",num3,"is smallest")
#     else:
#         print(num1,"is greater",num3,"is medium",num2,"is smallest")
# elif num2>num1 and num2>num3:
#     if num1>num3:
#         print(num2,"is greater",num1,"is medium",num3,"is smallest")
#     else:
#         print(num2,"is greater",num3,"is medium",num2,"is smallest") 
# elif num3>num1 and num3>num2:
#     if num2>num1:
#         print(num3,"is greater",num2,"is medium",num1,"is smallest")
#     else:
#         print(num3,"is greater",num1,"is medium",num2,"is smallest") 
# else:
#     print("something went wrong")  que3

# n=int(input("enter your number"))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i=i+1 que4

# n=int(input("enter your number"))
# n1=n
# m=int(input("enter your power"))
# i=1
# while i<m:
#     n=n*n1
#     i=i+1
# print(n)
# print(n**m)  que5

# n=int(input("enter your number"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")  que6


# n=int(input("enetr your number"))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#         i=i+1 que8

# 6=1+2+3
# n=int(input("enter your numbe"))
# i=1
# sum=0
# while i<n:
#     if n%i==0:
#         sum=sum+i
#     i=i+1
# if sum==n:
#     print("perfect number")
# else:
#     print('not perfect') que9

# n=int(input("enter your number"))
# m=int(input("enter your number"))
# i=2
# while i<m:
#     if n%i==0 and m%i==0:
#         print(i)
#         i=i+1 que10


# m=int(input("enter your number"))
# i=0
# second=0
# while i<2:
#     rem=m%10
#     i=i+1
#     m=m//10
# second=rem
# if second==7:
#     print("yes")
# else:
#     print("no") que13

# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))
# i=2
# if num1>num2:
#     max=num1
# else:
#     max=num2
# while i<max:
#     if num1%i==0 and num2%i==0:
#         break
#     i=i+1
# print(i,"least common factor") que12




# list=[1,2,3,4,5,6,7]
# n=int(input("enter your number"))
# if n in list:
#     print("present")
# else:
#     print("not")


a="neha"
if "n" in a:
    print("present")
else:
    print("not")

# list=["a",1,"2",5,"b","q"]
# n=int(input("enetr number"))
# i=-n
# while i<0:
#     print(list[i])
#     i=i+1

# list=[2,5,9,8,4,7]
# i=0
# while i<len(list):
#     if list[i]%2==0:
#         print(list[i],"even")

#     else:
#         print(list[i],"odd")
#     i=i+1
# que4

# # que3
# list=[1,5,3,6,5,8,89]
# a=0
# i=0
# while i<len(list):
#     if list[i]>a:
#         a=list[i]
#     i=i+1
# print(a)


# que5
# i=0
# while i<len(name):
#     print(name[i],"the",anumal[i],"is",age[i])
#     i=i+1
# a=[1,2,3,4,5,6]
# (1) a.append(7)
#     print(a)
# (2) a.remove(3)
#     print(3)
# (3) print(len(a))

# que6

# list=[2,3,4,5,6,7]
# i=0
# while i<len(list):
#     if list[i]%5==0:
#         print(list[i])
#     i=i+1
# que7

# dic={"a":10,"b":200,"c":300}

# sum=0
# for i in dic:
#     sum=sum+dic[i]
# print(sum)
# que8

# n=int(input("enter your number"))
# i=0
# while i<len(list):
#     if i<n:
#         list.remove(list[i])
#     i=i+1
# print(list)
# que9

# def fun1(c,b):
#     a=c+b
#     return a
# def fun2(e,f):
#     w=e+f+(fun1(1,2))
#     print(w)
# fun2(6,4)
# que11

# print:-
