class TorKham():
    lis = []
    lis_check= []
    count = 0
    canpass = True
    canwirte = True
    start = True

    def __init__(self):
        self.words = []

    def restart(self):
        global start,count,lis,lis_check,canpass,canwirte
        lis = []
        lis_check= []
        count = 0
        canpass = True
        canwirte = True
        start = True
        return "game restarted"

    def play(self, word):
        global start,count,lis,lis_check,canpass,canwirte
        
        lis = []
        lis_check= []
        count = 0
        canpass = True
        canwirte = True
        start = True
        
        self.words = word
        
        for i in range(len(self.words)):
            if self.words[i][0] == 'P':
                x = self.words[i].strip("P ") 

                if start == True and count==0:
                    start = False
                    lis.append(x)
                    print("'"+x+"'","->",lis)
            
                for j in lis:
                    if x.casefold() != j.casefold():
                        canpass= True
                    else:
                        canpass = False

                if canpass == True and start == False and count !=0 :
                
                    if x[0].casefold() == lis[count-1][-2].casefold() and x[1].casefold() == lis[count-1][-1].casefold():
                        lis.append(x)
                        print("'"+x+"'","->",lis)

                    else:
                        print("'"+x+"'","-> game over")
                count+=1

            elif self.words[i][0] == 'R':

                print(self.restart())

            elif self.words[i][0] != 'X':
                print("'"+S[i]+"'","is Invalid Input !!!")
                exit()


print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')
torkham = TorKham()
torkham.play(S)




        
        
        

