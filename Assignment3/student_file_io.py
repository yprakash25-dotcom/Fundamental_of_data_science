"""Program to collect student details from the user, save them to a file, and display the saved records."""


def write_student_records(filename: str, records: list[dict[str, str]]) -> None:
    """Write a list of student records to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Name,Roll,Grade\n")
        for record in records:
            file.write(f"{record['name']},{record['roll']},{record['grade']}\n")


def read_student_records(filename: str) -> list[dict[str, str]]:
    """Read student records from a text file and return a list of dictionaries."""
    students: list[dict[str, str]] = []
    with open(filename, "r", encoding="utf-8") as file:
        header = file.readline().strip().split(",")
        for line in file:
            if not line.strip():
                continue
            name, roll, grade = line.strip().split(",")
            students.append({"name": name, "roll": roll, "grade": grade})
    return students


def display_students(students: list[dict[str, str]]) -> None:
    """Display student records in a neat table format."""
    print("\nSaved student records:")
    print("Name\tRoll\tGrade")
    print("----\t----\t-----")
    for student in students:
        print(f"{student['name']}\t{student['roll']}\t{student['grade']}")


if __name__ == "__main__":
    print("Student File IO Program")
    records: list[dict[str, str]] = []

    for i in range(1, 4):
        print(f"\nEnter details for student {i}:")
        name = input("Name: ").strip()
        roll = input("Roll number: ").strip()
        grade = input("Grade: ").strip()
        records.append({"name": name, "roll": roll, "grade": grade})

    filename = "students.txt"
    write_student_records(filename, records)
    print(f"\nRecords saved to {filename}.")

    saved_students = read_student_records(filename)
    display_students(saved_students)
