# Student Attendance Analysis System

## Why I Built This

I'm a first-year student, and within the first few weeks, I kept hearing horror stories from seniors about attendance shortages. One guy in my hostel missed his finals because he was at 74.8% - literally 0.2% short of the 75% requirement. Another senior told me she spent the entire semester manually tracking attendance in a notebook and still miscalculated.

That got me paranoid. I didn't want to be that person scrambling before exams, so I built this tool early on. Better to automate it now than stress about it later.

## What It Actually Does

Pretty simple - you feed it a CSV file with attendance data (your reg number, subject names, classes attended, total classes), tell it what percentage you need (usually 75%), and it immediately shows which subjects are dangerous.

I check it every weekend. Takes maybe 10 seconds total, and I know exactly where I stand across all my courses.

## Main Features

**Processes Multiple Students**  
Started as just my personal tool, but then my roommates saw it and wanted to use it too. Now our CSV has data for about 8-10 people from our floor. Runs everyone's analysis at once.

**Adjustable Threshold**  
Most courses need 75%, but I've heard some departments require 80% for certain subjects, and some electives are more relaxed at 60%. You can change the percentage each time you run it.

**Handles Messy Data**  
The first version crashed when my friend copy-pasted his data wrong. Now it just skips problematic rows and keeps going. Shows you a warning but doesn't die completely.

**Only Shows Problems**  
Displays subjects where you're below threshold. If everything's fine, it just says "All clear" and exits. I don't need 50 lines telling me I'm doing okay in subjects I already know are safe.

## Technical Setup

**Requirements:**
- Python 3.x (I'm using 3.11, but anything 3.7+ should work)
- No external libraries - just the built-in `csv` module

**Files in This Repo:**
- `attendance_analyzer.py` - all the code
- `Student_Data.csv` - dummy data I created for testing
- `README.md` - you're reading it
- `STATEMENT.md` - formal problem statement (professor required this)

## Running the Program

1. Download/clone this
2. Put `attendance_analyzer.py` and your CSV in the same folder
3. Open terminal in that folder
4. Run:
```bash
   python attendance_analyzer.py
```
5. Enter your CSV filename (like `Student_Data.csv`)
6. Enter minimum percentage (like `75`)
7. Read the output

**Example Output:**
```
Enter CSV filename: Student_Data.csv
Enter minimum attendance %: 75

SHORTAGE ALERT for 25BCE10446:
- Operating Systems: 68.37% (134/196 classes)
```

## CSV Format

Your file needs these exact columns:  
`RegNo, SubjectName, Attended, ClassesLeft, Total`

Example from my test file:
```csv
25BCE10446,Data Structures,129,1,158
25BCE10446,Operating Systems,134,38,196
25BCE10447,Data Structures,145,1,158
```

**What Each Column Means:**
- **RegNo:** Registration number
- **SubjectName:** Course name (be consistent - "OS" vs "Operating Systems" counts as different courses)
- **Attended:** Classes attended so far
- **ClassesLeft:** Classes remaining this semester (I don't actually use this in calculations, but our university portal exports it this way)
- **Total:** Total classes for the entire semester

## How I Built This

**Design Choices:**

Kept it deliberately minimal - no pandas, no database, just CSV parsing. Reasons:

1. **CSV works everywhere** - Our college portal exports CSV, and everyone has Excel/Sheets
2. **Zero setup** - My friends can run this without installing anything extra
3. **Fast enough** - Processes hundreds of rows instantly

**The Math:**
```python
attendance_percentage = (classes_attended / total_classes) * 100
```

Round to 2 decimals because 74.99% vs 75.01% is a huge difference when you're on the edge.

**Error Handling:**

Catches these problems:
- File doesn't exist (wrong name)
- Non-numeric values in Attended/Total columns
- Empty rows
- Division by zero (if Total = 0)

When it hits a bad row, it prints a warning and moves on instead of crashing.

## Current Limitations

- **No data persistence:** Have to provide the CSV every time. Thought about adding a database but seemed unnecessary for a 10-second weekly check.
- **Terminal only:** Works fine for me, but I know it looks ancient. GUI would be nice.
- **No history:** Shows current status only, doesn't track changes over time.

## Future Ideas (Maybe)

**If I get time:**
- Export to PDF for easy sharing
- Calculate "classes needed to reach 75%" for shortage subjects
- Color output (red for critical, yellow for warning)

**Ambitious stuff:**
- Simple Tkinter GUI
- Automated email alerts - imagine a weekly email saying "Warning: 73% in Networks, attend next 4 classes"
- Web dashboard with charts

That email thing would actually be super useful. Set it as a Sunday night cron job and everyone gets their status automatically.

## What I Learned

First real Python project outside of classroom assignments. Some takeaways:

1. **Input validation matters** - People will type "seventy five" instead of "75"
2. **Files fail** - Always assume the file is missing or corrupted
3. **Variable names are important** - Came back to this code after a week and couldn't understand my own variables. Had to refactor.
4. **Documentation takes forever** - This README took almost as long as the actual code

## Contributing

If you're dealing with attendance tracking and want to improve this, go ahead and fork it. Ideas:

- Support different CSV formats (other colleges structure data differently)
- Build the GUI or email features
- Add proper unit tests (I didn't write any)
- Optimize for huge datasets (though I doubt anyone needs this)

## License

Use it however you want. If it helps you avoid attendance shortage, that's good enough for me.

---

**Note:** I'm a first-year CS student at VIT, so this code is probably not perfect. If you find bugs or have suggestions, I'm always learning!
