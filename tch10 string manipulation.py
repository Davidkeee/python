print("""
1
 2
  3
""")

text="Test.\nNext line."
print(text)

print('One', 'Two' * 2)
print('One' + 'Two' * 2)
print(len('0123456789'))

s = '0123456789'
print(s[3], ":", s[0:3], "-", s[2:])
print(s[:3], "-", s[3:], " ", s[3:10])
print(s[20:], s[2:1], s[1:1])

s = '987654321'
print(s[-1], s[-3])
print(s[-3:], s[:-3])
print(s[-100:-3], s[-100:3])

y = str(123)
x = "hello" * 3
print(x, y)
x = "hello" + "world"
y = len(x)
print(y, x)

x="hello"+\
   "to Python"+\
   "world"
for char in x :
    y=char
    print(y,':', end=' ')

x="hello world"
print(x[:2], x[:-2], x[-2:])
print(x[6], x[2:4])
print(x[2:-3], x[-4:-2])
