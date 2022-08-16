print("*** Fun with countdown ***")

lis = [int(x) for x in input("Enter List : ").split()]
temp = []
global ans
ans = []
last_ans = []
count = 0
for i in range(len(lis)):
    if lis[i]==1:
        count+=1
        temp.append(lis[i])
        ans.append(temp)
        
        
        temp =[]

    elif len(lis)-2 >= i :
        if lis[i] == lis[i+1]+1:
            temp.append(lis[i])
        else:
            temp =[]

    else:
        temp =[]
    
last_ans.append(ans)
last_ans.insert(0, count)
print(last_ans)