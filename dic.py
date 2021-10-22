# dic1={"brand":"suzuki","model":"dezire","year":"2020"}
# print(dic1)

# x=dic1["model"]
# print(x)

# y=dic1.get("model")
# print(y)

# for x in dic1:
#     print(x)


# for x in dic1:
#     print(dic1[x])

# for x in dic1.values():
#     print(x)

# for x,y in dic1.items():
#     print(x,y)


# dic1["year"]=2021
# print(dic1)


# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))

# Dict = {
#        'ball' : 'green',
#        'Ball': 'red'
#      }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])

# girl=dict(name="neha",age="18")
# print(girl)

 
# my_dict = {
#     'name': 'John',
#      1: [2, 4, 3]
#     }
# print(my_dict)

# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{
#      'A' : 'WELCOME',
#      'B' : 'To', 
#      'C' : 'DHARAMSALA'
#      }
# }
# print(Dic)


# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
#     }
    
# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic)

# dic= {
#     'Name': 'RAM',
#     'Age': 17,
#      }
# dic['student']={
#         'id':22, 
#         'place':'dharamsala'
#     }
# print(dic)

# dict1={"name":"neha","age":17}
# if "neha" in dict1.values():
#     print("yes")
# else:
#     print("no")

# dict1={"name":"neha","age":17}
# dict1["female"]="girl"
# print(dict1)

# classes ={
#     "room1":  6,
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# mydict=classes.copy()
# print(mydict)

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person)

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }

# del person['place']
# print(person)

# if True:
#     print("a")


# if True:
#     print("b")
# elif True:
#     print("d")
# elif False:
#     print("c")
# if True:
#     print("j")
# if False:
#     print("")
# else:
#     print("smji")


# for x in range(5):
#     print(x)
# for x in range(1,6):
#     print(x)
# for x in range(2,12,2):
#     print(x)
# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#     if list[i]%2==0:
#         print(i,list[i])
# fruit=["apple","banana","orange"]
# for i in fruit:
#      print(i)
#     if i=="orange":
#         print(i)
#         break
#     # print(i)

# for i in fruit:
#     print(i)
#     if i=="banana":
#         break

# for i in fruit:
#     if i=="banana":
#         print(i)
#         continue
#     print(i)

# names=["neha","tanjum","shaheen","thapa"]
#     for i in names:
#         if i=="tanjum":
#             continue
#     else:
#         print(i,"be happy")

#     if i=="shaheen":
#         break
#     else:
#         print(i)

# names=["neha","tanjum","shaheen","pretty"]
# sur_names=["prajapati","kadkod","siddiqui","thapa"]
# for name in names:
#     for sur_name in sur_names:
#         print(name,sur_name)