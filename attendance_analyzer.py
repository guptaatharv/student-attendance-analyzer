import csv

def load_student_data(filename):
    students = {}
    
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            
            for row in csv_reader:
                if not row or len(row) < 5:
                    continue
                
                try:
                    reg_no = row[0].strip()
                    subject = row[1].strip()
                    attended = int(row[2].strip())
                    classes_left = int(row[3].strip())
                    total_classes = int(row[4].strip())
                    
                    subject_info = [subject, attended, classes_left, total_classes]
                    
                    if reg_no not in students:
                        students[reg_no] = []
                    students[reg_no].append(subject_info)
                except:
                    print(f"Skipping invalid row")
                    continue
    
    except FileNotFoundError:
        print("Please check the filename and try again.")
        input("Press Enter to Exit...")
        return None
    
    return students

def find_attendance_shortage(students,MIN_ATTENDANCE):
    
    shortage_list = {}
    
    for reg_no, subjects in students.items():
        low_attendance_subjects = []
        
        for subject_info in subjects:
            subject_name, attended, classes_left, total = subject_info
            
            if total > 0:
                attendance_percent = (attended / total) * 100
            else:
                attendance_percent = 0
            
            if attendance_percent < MIN_ATTENDANCE:
                low_attendance_subjects.append(subject_name)
        
        if low_attendance_subjects:
            shortage_list[reg_no] = low_attendance_subjects
    
    return shortage_list

def print_report(shortage_list):
    
    if not shortage_list:
        print("\n Excellent! All students have good attendance.")
        print("   No one is below the 75% requirement.\n")
        input("\nPress Enter to Exit...")
    else:
        print()
        for reg_no, subjects in shortage_list.items():
            subject_list = ", ".join(subjects)
            print(f"{reg_no} has short att in subjects - {subject_list}")
        print()

def main():
    print("\n Student Attendance Analysis System")
    
    filename = input("Enter CSV filename: ").strip()
    MIN_ATTENDANCE = float(input("Enter Min. Attendance: "))

    student_data = load_student_data(filename)
    
    if student_data is None:
        return
    
    print(f" Successfully loaded data for {len(student_data)} students")
    
    shortage_report = find_attendance_shortage(student_data,MIN_ATTENDANCE)
    
    print_report(shortage_report)
    input("Press Enter to Exit")


main()

