from math import sqrt , acos as arccos , log10 as lg
while True:
    x = int(input('Введіть x '))
    if x < -1 :
        y=lg(abs(x+3.2))
        print(f'Значення y={y:.2f}')
        break
    elif x >= -1 and x <0:
        y=arccos(x)**2+abs(x**3)
        print(f'Значення y={y:.2f}')
        break
    elif x >0:
        y=2**sqrt(x)-(1/x+0.5)
        print(f'Значення y={y:.2f}')
        break
    else:
        print('Невірне значення x')