'''
(Convert letter grade to number)

Write a program that prompts the user to enter a letter grade A/a, B/b, C/c, D/d, or F/f
and displays its corresponding numeric value 4, 3, 2, 1, or 0.
'''
letter_grade = input('Enter a letter grade: ').upper()

if letter_grade == 'A':
    print("The numeric value for grade", letter_grade, "is 4")
elif letter_grade == 'B':
    print("The numeric value for grade", letter_grade, "is 3")
elif letter_grade == 'C':
    print("The numeric value for grade", letter_grade, "is 2")
elif letter_grade == 'D':
    print("The numeric value for grade", letter_grade, "is 1")
elif letter_grade == 'F':
    print("The numeric value for grade", letter_grade, "is 0")
else:
    print(letter_grade, "is an invalid grade")
