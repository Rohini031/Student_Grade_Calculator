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