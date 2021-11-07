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
    print(student['course'])

if __name__ =='__main__':
    main()