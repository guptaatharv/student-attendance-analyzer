# Student Attendance Analysis System

## Project Overview
As a college student, I often find it stressful to manually calculate attendance for every subject before exams to ensure I meet the 75% eligibility criteria. It is easy to miscalculate and miss the warning signs of a shortage.

I designed this **Student Attendance Analysis System** to solve this problem. It is a Python-based tool that automates attendance tracking by processing a raw CSV dataset of student records. It instantly identifies which students are falling below a specific attendance threshold (e.g., 75%) and generates a clear shortage report.

## Features
* **Bulk Processing:** Capable of analyzing records for any number of students and subjects simultaneously.
* **Custom Thresholds:** Users can define the minimum attendance percentage (e.g., 75%, 80%, or 60%) dynamically.
* **Shortage Detection:** Automatically filters and lists only the subjects where a student is lagging.
* **Robust Error Handling:** The system safely skips invalid rows or corrupt data without crashing.

## How It Works
1. **Input:** The user provides a CSV file containing student names, subjects, classes attended, and total classes.
2. **Configuration:** The user inputs the required minimum attendance percentage.
3. **Processing:** The system calculates the percentage for every subject using the formula: `(Attended / Total) * 100`.
4. **Output:** A console-based report displays exactly which students have a shortage and in which subjects.

## Project Structure
* `attendance_analyzer.py`: The main source code containing modular functions for data loading and analysis.
* `Student_Data.csv`: Sample dataset used for testing.
* `README.md`: Project documentation and usage guide.
* `STATEMENT.md`: Formal problem statement and scope.

## How to Run
1. Ensure you have Python installed on your system.
2. Place the `attendance_analyzer.py` and your CSV file (e.g., `Student_Data.csv`) in the same folder.
3. Open a terminal or command prompt in that folder.
4. Run the script:
   ```bash
   python attendance_analyzer.py
   ```
5. When prompted, enter the filename (e.g., `Student_Data.csv`) and your desired minimum attendance (e.g., `75`).

## CSV Data Format
The input CSV file must strictly follow this column structure:
`RegNo, SubjectName, Attended, ClassesLeft, Total`

**Example:**
```csv
25BCE10446,Data Structures,129,1,158
25BCE10446,Operating Systems,134,38,196
```

## Future Enhancements
* **Graphical User Interface (GUI):** Implement a Tkinter-based UI for better usability.
* **PDF Export:** Allow users to download the shortage report as a PDF file.
* **Email Alerts:** Integrate SMTP to automatically email students who are on the shortage list.