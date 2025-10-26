import pandas as pd
import numpy as np

# ================================
# Exercise: Pandas Dataframe Manipulation
# ================================

# Task 1: Create a sample DataFrame
# Create a DataFrame with student data

students_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Math': [85, 92, 78, 95, 88, 73],
    'Science': [90, 88, 85, 92, 79, 81],
    'English': [88, 85, 92, 89, 91, 78],
    'Grade': ['A', 'A', 'B', 'A', 'B', 'C']
}
df = pd.DataFrame(students_data)
print("Student DataFrame:")
print(df)


# ================================
# Task 2: Filter rows based on a condition
# Select only students with Math score > 80
# ================================

high_math = df[df['Math'] > 80]
print("\nStudents with Math > 80:")
print(high_math)


# ================================
# Task 3: Filter with multiple conditions
# Select students with Math > 80 AND Science > 85
# ================================

multiple_conditions = df[(df['Math'] > 80) & (df['Science'] > 85)]
print("\nStudents with Math > 80 AND Science > 85:")
print(multiple_conditions)


# ================================
# Task 4: Filter using isin()
# Select only students with Grade 'A' or 'B'
# ================================

grade_filter = df[(df['Grade'] == 'A') | (df['Grade'] == 'B')]
print("\nStudents with Grade A or B:")
print(grade_filter)


# ================================
# Task 5: Sort the DataFrame
# Sort by Math scores in descending order
# ================================

sorted_df = df.sort_values(by=['Math'], ascending=False)
print("\nDataFrame sorted by Math (descending):")
print(sorted_df)


# ================================
# Task 6: Calculate the average score for each student
# Add a new column 'Average' with the mean of Math, Science, and English
# ================================

# df['Average'] = (df["Math"] + df["Science"] + df["English"]) / 3
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
print("\nDataFrame with Average column:")
print(df)


# ================================
# Task 7: Group by Grade and calculate mean scores
# Group students by Grade and find mean Math score for each grade
# ================================

grouped = df.groupby('Grade')['Math'].mean()
print("\nMean Math score by Grade:")
print(grouped)


# ================================
# Task 8: Find the student with the highest average score
# Use the Average column you created
# ================================

top_student = df.loc[df['Average'].idxmax()]
print("\nTop student by average score:")
print(top_student)


# ================================
# Task 9: Count values in a column
# Count how many students are in each Grade
# ================================

grade_counts = df['Grade'].value_counts()
print("\nNumber of students per Grade:")
print(grade_counts)


# ================================
# Task 10: Replace values
# Replace Grade 'C' with 'Needs Improvement'
# ================================

df_copy = df.copy()  # Work with a copy
df_copy['Grade'] = df_copy['Grade'].replace("C", "Needs Improvement")
print("\nDataFrame with replaced grades:")
print(df_copy)
