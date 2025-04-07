#! /usr/bin/env python3

"Imprime Tabuada de 1 ao 10:"

# base = [1,2,3,4,5,6,7,8,9,10]

base = list(range(1, 11))

for numero in base:
    print("Tabuada do:",numero)
    for outro_numero in base:
        print(f"{numero} x {outro_numero} = {numero * outro_numero}")
    print("------------------------")
