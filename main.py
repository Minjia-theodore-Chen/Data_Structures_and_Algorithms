from enum import auto
from os import system, name
import time
from tokenize import group
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


class Solution:
    def getNum(self, base, l):
        val = 0
        for _ in range(l):
            val = base * val + 1
        return val

    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        for l in range(len("{:b}".format(n)), 1, -1):
            beg = 2
            end = n - 1
            while beg <= end:
                mid = (beg + end) // 2
                val = self.getNum(mid, l)
                if val == n:
                    return str(mid)
                elif beg == end:
                    break
                elif val < n:
                    beg = mid + 1
                else:
                    end = mid


def main():
    clear()
    A = Solution()
    print(A.smallestGoodBase("40"))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)
