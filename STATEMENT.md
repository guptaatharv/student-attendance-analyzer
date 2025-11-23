# Project Statement - Student Attendance Analysis System

## Problem Statement
In academic institutions, students are often required to maintain a minimum attendance percentage (typically 75%) to be eligible for final examinations. Monitoring this metric manually across multiple subjects for hundreds of students is a time-consuming and error-prone process. Students often struggle to calculate exactly which subjects they are short in, leading to last-minute detentions.

There is a need for an automated system that can ingest raw attendance data and instantly identify students who are falling below the mandatory threshold.

## Objective
To build a Python-based system that:
* Reads multi-student attendance records from a CSV file.
* Calculates subject-wise attendance percentages.
* Identifies subjects where a student has less than the required attendance.
* Generates a clear, text-based shortage report.

## Scope
* **Input:** The system accepts CSV files formatted with Student ID, Subject, Attended Classes, and Total Classes.
* **Processing:** It supports unlimited students and unlimited subjects per student.
* **Validation:** The system handles data inconsistencies (like empty rows) gracefully.
* **Output:** A console-based summary of students with shortages.

## Target Users
* **Students:** To self-evaluate their exam eligibility.
* **Faculty Members:** To quickly identify students who need academic counseling.
* **Academic Coordinators:** To generate shortage lists for detention purposes.

## Tools & Technologies
* **Language:** Python 3.x
* **Libraries:** `csv` (Built-in) for data handling.