a=int(input('first number:'))
b=int(input('second number:'))
c=int(input('third number:'))
plusroot=(-b+(b**2-4*a*c)**0.5)/(2*a)
minusroot=(-b-(b**2-4*a*c)**0.5)/(2*a)
print(minusroot)
print(plusroot)
#2
a=int(input('first number:'))
b=int(input('second number:'))
c=int(input('third number:'))
if a > b and a > c :
    print(a,'is the biggest')
elif b > a and b > c :
    print(b,'is the biggest')
elif c > a and c > b :
    print(c,'is the biggest')
#3
for number in range (1,51) :
  if number %2 == 0 : 
   print(number)
#4
n=int(input('enter a number'))
sum_of_series=n*(n+1)//2
print(sum_of_series)
#4



















































































