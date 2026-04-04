
marks = []  # Store marks for each subject

for i in range(6):  # Loop to read 6 subject marks
    m = float(input(f"Enter marks for subject {i+1}: "))  # Read marks for subject i+1
    marks.append(m)  # Add the mark to the list

total = sum(marks)  # Compute total marks
average = total / 6  # Compute average marks
percentage = (total / 600) * 100  # Convert total to percentage out of 600

if percentage >= 85:  # Distinction threshold
    grade = "Distinction"  # Assign grade for highest percentage
elif percentage >= 70:  # First division threshold
    grade = "First Division"  # Assign grade for first division
elif percentage >= 55:  # Second division threshold
    grade = "Second Division"  # Assign grade for second division
elif percentage >= 45:  # Third division threshold
    grade = "Third Division"  # Assign grade for third division
else:
    grade = "Fail"  # Assign fail grade if below 45%

print("\nTotal:", total)  # Display total marks
print("Average:", average)  # Display average marks
print("Percentage:", percentage)  # Display percentage
print("Grade:", grade)  # Display final grade
