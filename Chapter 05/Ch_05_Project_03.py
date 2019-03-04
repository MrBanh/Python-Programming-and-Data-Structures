'''
(Find the two highest scores)

Write a program that prompts the user to enter the number of students and each
student’s name and score, and finally displays the student with the highest
score and the student with the second-highest score. Assume that the number
of students is at least 2.
'''

num_of_students = int(input("Enter the number of students: "))
student_highest = ""
highest_score = 0
student_second_highest = ""
second_highest_score = 0

for i in range(num_of_students):
    current_student = input("Enter a student name: ")
    current_score = float(input("Enter a student score: "))

    # Determine if new score and student has highest score
    if current_score > highest_score:
        # Previous highest score and student is now second
        second_highest_score = highest_score
        student_second_highest = student_highest

        # Current student has highest score
        highest_score = current_score
        student_highest = current_student

    # If current student doesn't beat highest, but beats second highest
    elif current_score > second_highest_score:
        second_highest_score = current_score
        student_second_highest = current_student

print("Top two students:")
print(student_highest + "'s score is " + str(highest_score))
print(student_second_highest + "'s score is " + str(second_highest_score))
