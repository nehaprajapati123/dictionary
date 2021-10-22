dic =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
c=0
for i in dic:
    for j in dic[i]:
        c=c+1
print(c)

