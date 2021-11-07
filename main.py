from os import system, name
import math
import time


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    clear()
    student = {'name': 'Minjia', 'age': 25, 'course': ['Math', 'CompSci']}
    student.update({'name': 'Minjia CHEN', 'number': '17655229344'})
    del student['course']
    #test if I can push this properly
    print(student)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)
