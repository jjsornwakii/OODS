def bon(w):
    check_list = []
    count = 0
    last_count = 0
    myChar = ''
    for i in range(len(w)-1):
        if w[i] == w[i+1]:
            count+=1
    
        if(count >= last_count):
            myChar = w[i]
            last_count = count
            count = 0

    return (ord(myChar)-96)*4

secretCode = input("Enter secret code : ")


print(bon(secretCode))
        

