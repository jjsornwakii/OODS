from itertools import combinations

def findways(comb):
    c = comb
    lis = []
    temp = []
    start = False
    write = True
    sum = 0
    for i in list(c):

        for j in i:
            sum += j
            temp.append(j)
        
        if sum == 5 :
            temp.sort()
            for t in lis:
                if t != temp:
                    write = True
                else:
                    write = False

            if write == True:       
                lis.append(temp)

        sum = 0
        temp=[]
    
    return list(lis)
    
lis = [int(x) for x in input("Enter Your List : ").split()]
ans = []

if len(lis) >=3:
    comb = combinations(lis, 3)
    l = findways(comb)
    print(l)

else:
    print("Array Input Length Must More Than",len(lis))
    