
name = input("Enter your name: ")
mark1 = int(input("Enter marks in Subject 1: "))
mark2 = int(input("Enter marks in Subject 2: "))
mark3 = int(input("Enter marks in Subject 3: "))
total = mark1 + mark2 + mark3
average = total / 3
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
if average >= 40:
    print("Status: PASS")
else:
    print("Status: FAIL")

