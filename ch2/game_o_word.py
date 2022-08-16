class TorKham:

	def __init__(self):

		self.words = []

	def restart(self):

		 ### Enter Your Code Here ###

		return "game restarted"

	def play(self, word):

		 ### Enter Your Code Here ###

		return "game over"



torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')
lis = []
lis_check= []
count = 0
canpass = True
canwirte = True
start = True
 ### Enter Your Code Here ###

for i in range(len(S)):

        if S[i][0] == 'P':
            x = S[i].strip("P ") 

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
                
        

        elif S[i][0] == 'R':
            print("game restarted")
            lis = []
            lis_check= []
            count = 0
            canpass = True
            canwirte = True
            start = True

        elif S[i][0] != 'X':
            
            print("'"+S[i]+"'","is Invalid Input !!!")
            exit()

        
        
        

