from collections import Counter

def winner(vote_number_list):
    votes = Counter(vote_number_list)
    dic = {}

    for i in votes.values():
        dic[i]= []
        
    for (key,i) in votes.items():
        dic[i].append(key)


    maxVote = sorted(dic.keys(),reverse=True)[0]
    if len(dic[maxVote])>1:
        print ("*** No Candidate Wins ***")
    else:
        print((dic[maxVote]))
        

print("*** Election ***")
voter = int(input("Enter a number of voter(s) : "))

number_votes = list(map(int,input().strip().split()))[:voter] 

winner(number_votes)
