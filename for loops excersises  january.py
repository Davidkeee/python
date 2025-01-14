#1
for i in range(0,11,1):
    print(i)
#2
for i in range(10,-1,-1):
    print(i)
 
#3
for i in range(1,8):
        print('#'*i)
#4
rows=int(input('rows'))
columns=int(input('columns'))
for i in range(rows):
    for b in range(columns):
        print('#', end='')
    print()
 
 
#5
count=0
realcount=0
for i in range(0,11,1):
    count+=1
    mul=i*(count-1)
    realcount=count-1
    print(i,'x',realcount,'=',mul)
 
 
#6
for i in range(0,101,+2):
    print(i)
#7
for i in range(2,101,+2):
    minus=i-1
    print(minus)
 
#8
allnumber=0
for i in range(0,101,1):
    allnumber+=i
    print(allnumber)
#9
    allevennumber=0
for i in range(0,101,2):
    allevennumber+=i
    print(allevennumber)
 
alloddnumber=0
for b in range(2,101,2):
    minus=i-1
    alloddnumber+=minus
    print(alloddnumber)
 