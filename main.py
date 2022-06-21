from os import system, name
import time


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def make_new_temp_guess(Ploss: float, Tenv: float, Rth: float, *args, **kwargs):
    return Tenv+Rth*Ploss

def main():
    clear()
    
    Tnew: float = make_new_temp_guess(Tenv=30, Rth=0.1, Ploss=100, Pth=0)
    print(Tnew)
    # ddd
    # 0834 0910
    # 大爷我来啦！！


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)
