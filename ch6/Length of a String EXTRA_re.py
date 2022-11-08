def length(txt):     
    #Code Here
    if txt == "":
        return 0
    count = 1 + length(txt[1:])
    if count % 2 == 0:
        print(txt[0]+'~',end='')
    else:
        print(txt[0]+'*',end='')

    return count
    
inp = input("Enter Input : ")
inp = inp[::-1]
print("\n"+str(length(inp)))