#1. Scenario: You are working on a project that involves analyzing student performance data for a class of 32 students. The data is stored in a NumPy array named student_scores, where each row represents a student and each column represents a different subject. The subjects are arranged in the  following order: Math, Science, English, and History. Your task is to calculate the average score for each subject and identify the subject with the highest average score. 

import numpy as np

subjects = ['Math', 'Science', 'English', 'History']

num_students = int(input("Enter number of students: "))

student_scores = []

for i in range(num_students):
    print(f"\nEnter scores for Student {i + 1}:")
    
    math = float(input("Math: "))
    science = float(input("Science: "))
    english = float(input("English: "))
    history = float(input("History: "))
    
    student_scores.append([math, science, english, history])

student_scores = np.array(student_scores)

subject_averages = np.mean(student_scores, axis=0)

highest_avg_index = np.argmax(subject_averages)
highest_subject = subjects[highest_avg_index]
highest_avg_score = subject_averages[highest_avg_index]

print("\nStudent Scores Matrix:")
print(student_scores)

print("\nAnalysis Results:")
for i in range(len(subjects)):
    print(f"{subjects[i]} Average Score: {subject_averages[i]:.2f}")

print(f"\nSubject with the Highest Average Score: {highest_subject} ({highest_avg_score:.2f})")
