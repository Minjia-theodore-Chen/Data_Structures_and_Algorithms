from os import system, name
import math

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class signal:
    def __init__(self, frequency, amplitude) -> None:
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase_0 = None

    def phase(self, time, phase_0):
        if phase_0 != None:
            self.phase_0 = phase_0
            return self.phase_0 + 2 * time * self.frequency * math.pi
        else:
            print('Specify initial phase!')
            return None

def main():
    clear()
    Ntz_de = signal(50, 230)
    Phase = Ntz_de.phase(1, 0)
    print(Phase)

if __name__ =='__main__':
    main()