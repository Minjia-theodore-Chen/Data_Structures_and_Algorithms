from enum import auto
from os import system, name
import time
import numpy as np


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def make_new_temp_guess(Ploss: float, Tenv: float, Rth: float, *args, **kwargs):
    return Tenv+Rth*Ploss


def grouper(input: list[int]) -> np.ndarray:
    groups: list[list[int]] = list()
    i: int = 0

    while i < len(input):
        j: int = i
        while j < len(input)-1:
            if abs(input[j]-input[j+1]) < 3:
                j += 1
            else:
                break
        groups.append([i, j])
        j += 1
        i = j
    return np.array(groups)


def main():
    clear()
    lst = [0, 1, 2, 5, 8, 9, 10, 13, 14]
    print(grouper(lst), type(grouper(lst)))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)
