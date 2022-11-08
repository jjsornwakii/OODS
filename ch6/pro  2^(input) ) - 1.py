

def showBi(digit,dec,i=0):
    t = ""

    if digit < 0 :
        return "Only Positive & Zero Number ! ! !"

    elif i < dec :
        bi = str(find(i))
        t = '0'*(digit-len(bi))
        return t + bi +"\n" + showBi(digit,dec,i+1)

    else:
        return ""

def find( decimal_number ):
    if decimal_number == 0:
        return 0
    else:
        return (decimal_number % 2 + 10 * find(int(decimal_number // 2)))      

inp = int(input("Enter Number : "))
print(showBi(inp,2**inp))