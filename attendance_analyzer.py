import csv

def load_data(filename):
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
                    
                    sub_info = [subject, attended, classes_left, total_classes]
                    
                    if reg_no not in students:
                        students[reg_no] = []
                    students[reg_no].append(sub_info)
                except:
                    print(f"Skipping")
                    continue
    
    except FileNotFoundError:
        print("Please check the filename and try again.")
        input("Press Enter to Exit...")
        return None
    
    return students

def find_shortage(students,minimum_attendance):
    
    shortage_list = {}
    
    for reg_no, subjects in students.items():
        low_attendance_subjects = []
        
        for subject_info in subjects:
            subject_name, attended, classes_left, total = subject_info
            
            if total > 0:
                attendance_percent = (attended / total) * 100
            else:
                attendance_percent = 0
            
            if attendance_percent < minimum_attendance:
                low_attendance_subjects.append(subject_name)
        
        if low_attendance_subjects:
            shortage_list[reg_no] = low_attendance_subjects
    
    return shortage_list

def print_output(shortage_list):
    
    if not shortage_list:
        print(" No one is below the 75% ,requirement")
        input("Press Enter to Exit...")
    else:
        print()
        for reg_no, subjects in shortage_list.items():
            subject_list = ", ".join(subjects)
            print(f"{reg_no} has short attendance in subjects - {subject_list}")
        print()

def main():
    print("Student Attendance System")
    
    filename = input("Enter CSV filename: ").strip()
    minimum_attendance = float(input("Enter Min. Attendance: "))

    student_data = load_data(filename)
    
    print(f"loaded data for {len(student_data)} student")
    
    shortage_report = find_shortage(student_data,minimum_attendance)
    
    print_output(shortage_report)
    input("Press Enter to Exit")


main()


