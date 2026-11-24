def average(marks):
    return sum(marks) / len(marks)

def grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 65:
        return "C"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def is_pass(marks):
    return all(mark >= 40 for mark in marks)

# Main program

name = input("Enter student name: ")

n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    mark = int(input("Enter marks: "))
    marks.append(mark)

avg = average(marks)

print("\n----Student Details----")
print("Student Name:", name)
print("Average Marks:", avg)
print("Grade:", grade(avg))

if is_pass(marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
    