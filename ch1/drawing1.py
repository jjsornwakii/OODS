print("*** Fun with Drawing ***")
n = input("Enter input : ")
N = (int(n)*2)-1 + int(n)*2-2
n = N
count = 0
symbol = '#'
for i in range(int(N/2)+1):
    count = i
    symbol = '#'

    for j in range(count):
            print(symbol,end='')
            if(symbol=='#'): symbol = '.'
            elif(symbol=='.'): symbol = '#'
        
    for k in range(N-i*2):
            n = N-i*2
            print(symbol,end='')

    for j in range(count):       
            if(symbol=='#'): symbol = '.'
            elif(symbol=='.'): symbol = '#'
            print(symbol,end='')
    
    print("")   

for i in range(int(N/2)):
    count-=1
    symbol = '#'
            
    for j in range(count):
            print(symbol,end='')
            if(symbol=='#'): symbol = '.'
            elif(symbol=='.'): symbol = '#'   

    for k in range(n+(i+1)*2):
            print(symbol,end='')

    for j in range(count):
            if(symbol=='#'): symbol = '.'
            elif(symbol=='.'): symbol = '#'
            print(symbol,end='')
            
    print("")   