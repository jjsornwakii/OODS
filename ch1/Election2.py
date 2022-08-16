from collections import Counter

print("*** Election ***")
voter = int(input("Enter a number of voter(s) : "))

number_votes = list(map(int,input().strip().split()))[:voter]

vote_count=Counter(number_votes)
 

max_votes=max(vote_count.values())
 

lst=[i for i in vote_count.keys() if vote_count[i]==max_votes]
 

print(sorted(lst)[0])