"""
(Print a table) 
Write a program that displays the following table:

a      a^2    a^3
1      1      1
2      4      8
3      9      27
4      16     64
"""

print(f'{"a":<5}{"a^2":<7}{"a^3":<7}')      # Display heading

for i in range(1, 5):       # 1 up to 5, but not including 5
    print(f'{i:<5}{i**2:<7}{i**3:<7}')
