def staircase(n,i=1):
    #code here
    t = ""
    
    if n != 0:        
        if n > 0 :
            t = '_'*(n-1)
            t = t + '#'*i
            n = n -1
 
        else:
            t = '_'*(i-1)
            t = t + '#'*(-1*n)
            n = n+1

        return t +'\n'+staircase(n,i+1)        ### ค่า n ลดลงเรื่อยๆ

    elif n==0 and i ==1:
        return str("Not Draw!")

    else:
        return ""




print(staircase(int(input("Enter Input : "))))