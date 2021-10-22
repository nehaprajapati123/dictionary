list=    [
        {"first":"1"}, 
        {"second": "2"}, 
        {"third": "1"}, 
        {"four": "5"}, 
        {"five":"5"}, 
        {"six":"9"},
        {"seven":"7"}
    ]
list2=[]
for i in list:
    for j in i:
        if (i[j]) not in list2:
           list2. append((i[j]) )
print(list2)
