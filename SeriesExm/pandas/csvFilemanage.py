import pandas as pd
import os

# Define absolute path to the CSV file
csv_path = '/home/tufa15/Documents/PYTHON_pgms/SeriesExm/pandas/results.csv'

# Check if the file exists before attempting to read it
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV file not found at {csv_path}")

# Load data from the CSV file, skipping the first three rows
try:
    df = pd.read_csv(csv_path, skiprows=3)
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit(1)
except Exception as e:
    print(f"Error loading CSV file: {e}")
    exit(1)

# Display students with 'S' grade in all subjects
students_with_s_grade = df[(df.iloc[:, 2:] == 'S').all(axis=1)][['REGISTER NO', 'NAME']]
print("Students with 'S' grade in all subjects:")
print(students_with_s_grade)

# Compute pass percentage for each subject (non-'F' grades)
subject_pass_percentages = (df.iloc[:, 2:] != 'F').mean() * 100
print("\nPass percentage for each subject:")
print(subject_pass_percentages)

# Display students who have passed all subjects
students_passed_all_subjects = df[(df.iloc[:, 2:] != 'F').all(axis=1)][['REGISTER NO', 'NAME']]
print("\nStudents who have passed all subjects:")
print(students_passed_all_subjects)
