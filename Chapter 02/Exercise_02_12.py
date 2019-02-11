'''
(Print a table)
Write a program that displays the following table:

a      b       pow(a, b)
1      2       1
2      3       8
3      4       81
4      5       1024
5      6       15625

'''

print(f'{"a":<5} {"b":<5} {"pow(a, b)":<5}')

for i in range(1, 6):
    a = i
    b = i + 1
    result = a ** b

    print(f'{a:<5} {b:<5} {result:<5}')
