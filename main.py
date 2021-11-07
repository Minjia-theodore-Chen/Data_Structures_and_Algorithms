from os import system, name
import math

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    clear()
    student = {'name' : 'Minjia','age' : 25, 'course' : ['Math', 'CompSci']}
    student['number'] = '1765229344'
    print(student)

if __name__ =='__main__':
    main()