import csv

total_days = 0
present_days = 0

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_days += 1
        if row['status'] == 'Present':
            present_days += 1

attendance_percentage = (present_days / total_days) * 100
print("Attendance Percentage:", attendance_percentage)
