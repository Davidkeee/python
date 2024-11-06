total = 0
count = 0

while True:
    user_input = input("Enter an integer (or press Enter to stop): ")
    if user_input == "":
        break
    num = int(user_input)
    total += num
    count += 1

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No numbers entered.")

total = 0
count = 0

while True:
    num = int(input("Enter an integer (negative number to stop): "))
    if num < 0:
        break
    total += num
    count += 1

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No numbers entered.")

total = 0
count = 0

while True:
    grade = int(input("Enter a test grade (negative number to stop): "))
    if grade < 0:
        break
    total += grade
    count += 1

if count > 0:
    average = total / count
    print("Average grade:", average)
    
    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    print("Letter grade:", letter_grade)
else:
    print("No grades entered.")

num = int(input("Enter an integer: "))

while num >= 0:
    print(num)
    num -= 1

num = int(input("Enter an integer: "))

for i in range(0, num + 1, 2):
    print(i)
