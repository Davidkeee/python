sport=["soccer","volleyball"]
fav= input("what is your favourite sport?")
sport.sort()
print(sport)

subjects=["english","math","irish","engineering"]
dislike= input("what subjects do you dislike:english,math irish or engineering?")
if dislike in subjects:
    subjects.remove(dislike)
    subjects.sort()
    print(subjects)
else:
    print("not a subjects asked")
    
colours=["red","blue","yellow","pink","black","white","purple","orange","turqoise","green"]


