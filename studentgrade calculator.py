# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to determine grade
def find_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

# Function to display result
def display_result(name, average, grade):
    print("\n----- Result -----")
    print(f"Student Name: {name}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")

# Main Program
name = input("Enter student name: ")
marks = []

# Taking 3 subject marks
for i in range(3):
    score = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)

average = calculate_average(marks)
grade = find_grade(average)
display_result(name, average, grade)
