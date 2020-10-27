#%%


real = 100
aprox = .888
tolerancia = .01

step = 1.0

absoluto = abs(aprox - real)
relativo = absoluto / real
porcentual = relativo * 100

n = 100099

for i in range(0, n):
    temporal_aprox = aprox
    aprox += step
    absoluto = abs(aprox - real)
    if aprox > real:
        print("--------------\npaso:",i)
        step = step/ 2
        print('step:',step)
        print('Aproximado que se pasa del valor real:', aprox)
        aprox = temporal_aprox
        print('Aproximado regresado un paso:', aprox)
        print('real:',real)
    if abs(aprox - real) <= tolerancia:
        break


print('\naproximado:', aprox, 'error:', absoluto)
print('relativo:', relativo)
print("porcentual:", porcentual)
print("%s")
# %%