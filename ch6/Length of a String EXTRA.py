def length(txt):     
    #Code Here
    count = 0
    
    if txt != ""  :
        c = ''
        t=""
        if txt[0]=='*':
            c = '~'
            txt = txt[1:]
        elif txt[0]=='~':
            c = '*'
            txt = txt[1:]
        
        else:
            c='*'

        if txt != "":
            t = txt[0]
            t = t+c
            print(t,end='')
            t = t[1]+txt[1:]

        
        count = 1 + length(t)
        
        return count
    
    elif txt == "" :
        return count

print("\n",length(input("Enter Input : "))-1,sep="")
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)