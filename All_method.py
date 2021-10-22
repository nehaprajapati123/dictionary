emotions={"happy":"sad",
"proud":"guilty",
"dissappointing":"successful"}

# print(emotions)
# print(emotions["proud"])
# print(len(emotions))
# print(type(emotions))

# x=emotions["happy"]
# print(x)

# x=emotions.get("happy")
# print(x)

# x=emotions.keys()
# print(x)

#={"happy":"sad",
#"proud":"guilty",
#"dissappointing":"successful"}

# emotions["proud"]="crying"
# print(emotions)

# x=emotions.values()
# print(x)

# x=emotions.items()
# print(x)

# emotions.update({"happy":"glad"})
# print(emotions)

# emotions.pop("happy")
# print(emotions)

# emotiontis.popitem()
# print(emoons)

# del emotions
# print(emotions)

# emotions.clear()
# print(emotions)

# loop..................................................
emotions={"happy":"sad",
"proud":"guilty",
"dissappointing":"successful"}
# for x in emotions:
#     print(x)

# for x in emotions.values():
#     print(x)

# for x in emotions:
#     print(emotions[x])

for x in emotions.keys():
    print(x)

# for x,y in emotions.items():
#     print(x,y)

# copy.....................................................
emotions={"happy":"sad",
"proud":"guilty",
"dissappointing":"successful"}

# x=emotions.copy()
# print(x)

# c=dict(emotions)
# print(c)



# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# dict1={"one","two","three","four","five"}
# dict2={1,2,3,4,5}
# dict1.update(dict2)
# print(dict1)

# list=[1,"two"]
# dic={3:"three",4:"four",5:"five"}
# dic.update([list])
# list.append([dic])
# print(dic)
# print(list)