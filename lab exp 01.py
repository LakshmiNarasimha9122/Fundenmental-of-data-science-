#1. Scenario: You are working on a project that involves analyzing student performance data for a class of 32 students. The data is stored in a NumPy array named student_scores, where each row represents a student and each column represents a different subject. The subjects are arranged in the  following order: Math, Science, English, and History. Your task is to calculate the average score for each subject and identify the subject with the highest average score. 

import numpy as np
import pandas as pd

subjects = ['Math', 'Science', 'English', 'History']

data = pd.read_csv("student_scores.csv")

student_scores = data[subjects].to_numpy()

subject_averages = np.mean(student_scores, axis=0)

highest_avg_index = np.argmax(subject_averages)
highest_subject = subjects[highest_avg_index]
highest_avg_score = subject_averages[highest_avg_index]

print("Student Scores Matrix:")
print(student_scores)

print("\nAnalysis Results:")
for i in range(len(subjects)):
    print(f"{subjects[i]} Average Score: {subject_averages[i]:.2f}")

print(f"\nSubject with the Highest Average Score: {highest_subject} ({highest_avg_score:.2f})")
