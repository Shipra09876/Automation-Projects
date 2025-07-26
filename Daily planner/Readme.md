# 🗓️ Daily Task Scheduler (Automation Project)
This project is a simple Python-based automation tool that reads tasks from a CSV file, schedules them intelligently, and writes a daily planner into a .txt file.

# ✅ Features
- Accepts user-defined tasks with durations via CSV file

- Automatically schedules tasks from 9:00 AM onward

- Outputs a nicely formatted daily planner text file

- Uses pandas for CSV handling and automation

- Folder structure is automatically created if not present

# 🛠️ Technologies Used
Python 3.x

pandas

datetime

os

# 📦 Requirements
- Install dependencies:
    pip install pandas

# ▶️ How to Run
- Place your tasks.csv file in the same directory as main.py.

- Run the script:

- python main.py
- Check the output:

- A folder named Daily planner/ will be created.

- The scheduled tasks will be saved inside Daily planner/output.txt.

# 📄 Example Output in output.txt

09:00 AM - 10:30 AM: Write Report
10:30 AM - 11:00 AM: Check Email
11:00 AM - 12:00 PM: Study

# 🧠 How it Works
- Reads all tasks and durations from tasks.csv

- Starts scheduling from 9:00 AM

- Adds each task one by one by incrementing start time using datetime.timedelta

- Saves the final output in a human-readable format inside a .txt file

