def Min(lis):
    l = lis
    if len(l) == 1:
        return l[0]
    else:
        return min(l[0],Min(l[1:]))

inp = [int(x) for x in input("Enter Input : ").split()]
m = Min(inp)
print("Min :",m)

