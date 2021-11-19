from os import system, name
import pandapower as pp
import pandapower.networks as nw
import time


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    clear()
    net = nw.simple_four_bus_system()
    print(net.bus)
    # ddd
    # 0834 0910
    # 大爷我来啦！！


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)
