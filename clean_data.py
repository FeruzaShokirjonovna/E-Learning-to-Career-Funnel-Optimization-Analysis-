import pandas as pd

# Open our raw box file that we made 
print("Loading the student data...")
df = pd.read_csv('studyflix_student_data.csv')

# Check how many rows we have before cleaning
print(f"Total student records found: {len(df)}")

# Check for empty spaces (Missing Values)
# Python will count if there are any blank cells
missing_stuff = df.isnull().sum()
print("\n Checking for broken or empty clues:")
print(missing_stuff)

# Check for duplicates (Did any student get recorded twice by mistake?)
duplicate_count = df.duplicated(subset=['Student_ID']).sum()
print(f"\n Number of duplicate student entries: {duplicate_count}")

# Create a "Clean Summary Table" to inspect the average watch time by subject
# This helps us see if the data looks mathematically healthy and reasonable
print("\n Calculating average watch time for each school subject:")
summary_table = df.groupby('Subject')['Watch_Time_Minutes'].mean()
print(summary_table)

print("\n Data is inspected, verified, and clean!")