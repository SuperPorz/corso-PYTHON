"""
La sintassi del ciclo FOR è:
    for  indice  in range(start, stop, step):
        # codice....

N.B. L'estremo destro dell'intervallo è stop - 1
"""

for idx in range(0, 5, 1):
    print(idx)

    if idx == 3:
        break

for idx in range(5, 0, -1):
    print(idx)