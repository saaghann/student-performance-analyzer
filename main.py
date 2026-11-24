import csv
import os
import matplotlib.pyplot as plt
from openpyxl import Workbook

# ==============================================
# 1. CALCULATE GRADE
# ==============================================

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# ==============================================
# 2. CALCULATE RESULTS
# ==============================================

def calculate_results(marks):

    total = sum(marks)
    maximum = len(marks) * 100
    percentage = (total / maximum) * 100
    average = total / len(marks)

    return total, maximum, percentage, average


# ==============================================
# 3. GET STUDENT MARKS
# ==============================================

def get_student_marks(subjects):

    marks = []

    for subject in subjects:

        while True:
            try:
                score = int(input(f"Enter {subject} marks (0-100): "))

                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("Invalid marks! Enter between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    return marks


# ==============================================
# 4. ANALYZE PERFORMANCE
# ==============================================

def analyze_performance(subjects, marks):

    highest_marks = max(marks)
    lowest_marks = min(marks)

    highest_index = marks.index(highest_marks)
    lowest_index = marks.index(lowest_marks)

    highest_subject = subjects[highest_index]
    lowest_subject = subjects[lowest_index]

    failed_subjects = 0

    for score in marks:
        if score < 40:
            failed_subjects += 1

    average = sum(marks) / len(marks)

    if average > 85:
        consistency = "Performing consistently well"
    else:
        consistency = "Focus on improving consistency"

    return (
        highest_subject,
        lowest_subject,
        highest_marks,
        lowest_marks,
        failed_subjects,
        consistency
    )


# ==============================================
# 5. GENERATE SUBJECT INSIGHTS
# ==============================================

def generate_insights(subjects, marks):

    print("\n========== SUBJECT INSIGHTS ==========")

    excellent_count = 0

    for subject, score in zip(subjects, marks):

        if score >= 90:
            print(f"Excellent performance in {subject}!")
            excellent_count += 1

        elif score >= 75:
            print(f"Good performance in {subject}.")

        elif score >= 50:
            print(f"You need more practice in {subject}.")

        else:
            print(f"You need to improve significantly in {subject}.")

    print("\nSubjects with 90+ marks:", excellent_count)


# ==============================================
# 6. DISPLAY REPORT
# ==============================================

def display_report(
    student_name,
    total,
    maximum,
    percentage,
    average,
    grade,
    highest_subject,
    highest_marks,
    lowest_subject,
    lowest_marks,
    remark,
    failed_subjects,
    consistency
):

    print("\n======================================")
    print("        PERFORMANCE REPORT")
    print("======================================")

    print("Student Name:", student_name)
    print("Total Marks:", total)
    print("Maximum Marks:", maximum)
    print("Percentage:", round(percentage, 2), "%")
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)

    print("Highest Subject:", highest_subject, "-", highest_marks)
    print("Lowest Subject:", lowest_subject, "-", lowest_marks)

    print("Failed Subjects:", failed_subjects)
    print("Consistency:", consistency)
    print("Overall Remark:", remark)

    status = "PASS" if percentage >= 40 else "FAIL"
    print("Status:", status)

    print("======================================")


# ==============================================
# 7. SAVE REPORT TO FILE
# ==============================================

def save_report(
    student_name,
    total,
    maximum,
    percentage,
    average,
    grade,
    highest_subject,
    highest_marks,
    lowest_subject,
    lowest_marks,
    remark,
    failed_subjects,
    consistency
):

    with open("report.txt", "w") as file:

        file.write("========== STUDENT PERFORMANCE REPORT ==========\n")
        file.write(f"Student Name: {student_name}\n")
        file.write(f"Total Marks: {total}/{maximum}\n")
        file.write(f"Percentage: {percentage:.2f}%\n")
        file.write(f"Average: {average:.2f}\n")
        file.write(f"Grade: {grade}\n")
        file.write(f"Highest Subject: {highest_subject} ({highest_marks})\n")
        file.write(f"Lowest Subject: {lowest_subject} ({lowest_marks})\n")
        file.write(f"Failed Subjects: {failed_subjects}\n")
        file.write(f"Consistency: {consistency}\n")
        file.write(f"Overall Remark: {remark}\n")
        file.write(f"Status: {'PASS' if percentage >= 40 else 'FAIL'}\n")

    print("\nStudent report saved to report.txt successfully!")


# ==============================================
# 8. SINGLE STUDENT ANALYSIS
# ==============================================

def main():

    print("\n========== SINGLE STUDENT ANALYSIS ==========")

    # Student name validation
    while True:

        student_name = input("Enter student name: ").strip()

        if student_name:
            break
        else:
            print("Name cannot be empty!")

    subjects = [
        "Maths",
        "Python",
        "DBMS",
        "Statistics",
        "Data Science"
    ]

    marks = get_student_marks(subjects)

    total, maximum, percentage, average = calculate_results(marks)

    grade = calculate_grade(percentage)

    (
        highest_subject,
        lowest_subject,
        highest_marks,
        lowest_marks,
        failed_subjects,
        consistency
    ) = analyze_performance(subjects, marks)

    if percentage >= 90:
        remark = "Outstanding performance!"
    elif percentage >= 80:
        remark = "Very good performance!"
    elif percentage >= 70:
        remark = "Good performance!"
    elif percentage >= 50:
        remark = "Average performance. Keep practicing."
    else:
        remark = "Needs significant improvement."

    display_report(
        student_name,
        total,
        maximum,
        percentage,
        average,
        grade,
        highest_subject,
        highest_marks,
        lowest_subject,
        lowest_marks,
        remark,
        failed_subjects,
        consistency
    )

    save_report(
        student_name,
        total,
        maximum,
        percentage,
        average,
        grade,
        highest_subject,
        highest_marks,
        lowest_subject,
        lowest_marks,
        remark,
        failed_subjects,
        consistency
    )

    generate_insights(subjects, marks)

    # Visualization
    plt.figure(figsize=(9, 5))
    plt.barh(subjects, marks)

    plt.title(f"Subject Performance of {student_name}")
    plt.xlabel("Marks")
    plt.ylabel("Subjects")
    plt.xlim(0, 100)
    plt.grid(axis="x", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()

# ==============================================
# SAVE STUDENT DATA TO CSV
# ==============================================

def save_students_to_csv(students):

    filename = "students.csv"

    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as file:

        writer = csv.writer(file)

        # Write header only when file is new or empty
        if not file_exists or os.path.getsize(filename) == 0:

            writer.writerow([
                "Student Name",
                "Total Marks",
                "Percentage",
                "Average",
                "Grade"
            ])

        for student in students:

            writer.writerow([
                student["name"],
                student["total"],
                round(student["percentage"], 2),
                round(student["average"], 2),
                student["grade"]
            ])

    print("\nStudent records saved to students.csv successfully!")

# ==============================================
# 9. MULTIPLE STUDENT MANAGEMENT
# ==============================================

def manage_multiple_students():

    students = []

    # Validate number of students
    while True:
        try:
            number_of_students = int(
                input("\nHow many students do you want to analyze? ")
            )

            if number_of_students > 0:
                break
            else:
                print("Enter a number greater than zero.")

        except ValueError:
            print("Please enter a valid integer.")

    subjects = [
        "Maths",
        "Python",
        "DBMS",
        "Statistics",
        "Data Science"
    ]

    # Collect student information
    for i in range(number_of_students):

        print(f"\n========== STUDENT {i + 1} ==========")

        # Name validation
        while True:
            name = input("Enter student name: ").strip()

            if name:
                break
            else:
                print("Name cannot be empty!")

        marks = get_student_marks(subjects)

        total, maximum, percentage, average = calculate_results(marks)

        grade = calculate_grade(percentage)

        student = {
            "name": name,
            "marks": marks,
            "total": total,
            "percentage": percentage,
            "average": average,
            "grade": grade
        }

        students.append(student)

    # Display class result
    print("\n==============================================")
    print("               CLASS RESULTS")
    print("==============================================")

    for student in students:

        print(
            f"Name: {student['name']} | "
            f"Total: {student['total']}/500 | "
            f"Percentage: {student['percentage']:.2f}% | "
            f"Grade: {student['grade']}"
        )

    # Calculate class average
    total_percentage = sum(student["percentage"] for student in students)

    class_average = total_percentage / len(students)

    print("\nClass Average:", round(class_average, 2), "%")

    # Find topper
    topper = max(students, key=lambda student: student["percentage"])

    print("\n========== CLASS TOPPER ==========")
    print("Topper Name:", topper["name"])
    print("Topper Percentage:", round(topper["percentage"], 2), "%")
    print("Topper Grade:", topper["grade"])

    # Ranking
    ranked_students = sorted(
        students,
        key=lambda student: student["percentage"],
        reverse=True
    )

    print("\n========== STUDENT RANKING ==========")

    for rank, student in enumerate(ranked_students, start=1):

        print(
            f"{rank}. {student['name']} - "
            f"{student['percentage']:.2f}% ({student['grade']})"
        )
# Save student records to CSV
    save_students_to_csv(students)

# ==============================================
# VIEW SAVED STUDENT RECORDS
# ==============================================

def view_saved_students():

    filename = "students.csv"

    if not os.path.exists(filename):
        print("\nNo student records found!")
        return

    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        print("\n========== SAVED STUDENT RECORDS ==========")

        records_found = False

        for student in reader:

            records_found = True

            print(
                f"Name: {student['Student Name']} | "
                f"Total: {student['Total Marks']} | "
                f"Percentage: {student['Percentage']}% | "
                f"Average: {student['Average']} | "
                f"Grade: {student['Grade']}"
            )

        if not records_found:
            print("No student records available.")

# ==============================================
# CLASS PERFORMANCE VISUALIZATION
# ==============================================

def visualize_class_performance():

    filename = "students.csv"

    if not os.path.exists(filename):
        print("\nNo student records found!")
        return

    names = []
    percentages = []
    grades = []

    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        # Check CSV headers
        if not reader.fieldnames:
            print("\nCSV file is empty!")
            return

        required_columns = [
            "Student Name",
            "Percentage",
            "Grade"
        ]

        if not all(column in reader.fieldnames for column in required_columns):
            print("\nCSV column names do not match the expected format.")
            print("Expected columns:", required_columns)
            print("Found columns:", reader.fieldnames)
            return

        for student in reader:

            try:
                names.append(student["Student Name"])
                percentages.append(float(student["Percentage"]))
                grades.append(student["Grade"])

            except (ValueError, TypeError, KeyError):
                print("Skipping an invalid CSV record.")

    if not names:
        print("\nNo valid student records available!")
        return

    # Chart 1: Student Percentage Comparison

    plt.figure(figsize=(10, 5))

    plt.bar(names, percentages)

    plt.title("Student Performance Comparison")
    plt.xlabel("Students")
    plt.ylabel("Percentage")

    plt.ylim(0, 100)
    plt.xticks(rotation=30)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()

    # Chart 2: Grade Distribution

    grade_counts = {}

    for grade in grades:
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    plt.figure(figsize=(7, 7))

    plt.pie(
        grade_counts.values(),
        labels=grade_counts.keys(),
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Grade Distribution")
    plt.show()

# ==============================================
# EXPORT STUDENT DATA TO EXCEL
# ==============================================

def export_to_excel():

    filename = "students.csv"

    if not os.path.exists(filename):
        print("\nNo student records found!")
        return

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Student Results"

    with open(filename, "r", newline="") as file:

        reader = csv.reader(file)

        for row in reader:
            sheet.append(row)

    workbook.save("students.xlsx")

    print("\nStudent records exported to students.xlsx successfully!")

# ==============================================
# MAIN MENU
# ==============================================

def menu():

    while True:

        print("\n================================")
        print("   STUDENT PERFORMANCE ANALYZER")
        print("================================")

        print("1. Analyze a single student")
        print("2. Analyze multiple students")
        print("3. View saved student records")
        print("4. Visualize class performance")
        print("5. Export records to Excel")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":

            main()

        elif choice == "2":

            manage_multiple_students()

        elif choice == "3":

            view_saved_students()

        elif choice == "4":
            visualize_class_performance()

        elif choice == "5":
            export_to_excel()

        elif choice == "6":
           print("\nThank you for using Student Performance Analyzer!")
           break
        

        else:

            print("\nInvalid choice! Please select 1, 2, 3, 4 or 5.")
        break
# ==============================================
# 11. PROGRAM EXECUTION
# ==============================================

if __name__ == "__main__":
    menu()
