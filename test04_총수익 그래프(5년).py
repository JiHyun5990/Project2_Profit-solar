import math
import matplotlib.pyplot as plt
import numpy as np

PV = 491.4
UR = 0.1666
d = 0.008
SMP = 100
REC = 50
r = 0.045

input_year_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                   21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                   31, 32, 33, 34, 35]
Benefit = []

print(input_year_list)
print(input_year_list[0])

for i in input_year_list:
    def func_formulaA(input_year):
        sum = 0
        for n in range(0, input_year + 1):
            formulaD = math.pow(1 - d, n)
            formulaR = math.pow(1 + r, n)
            sum += (UR * formulaD * (SMP + REC) / formulaR)
        return sum

    formulaA = func_formulaA(i)
    Result = PV * 8760 * formulaA
    Benefit.append(Result/100000)

print('\n')
print(Benefit[0])
print(Benefit[1])
print(Benefit[2])
print(Benefit[3])
print(Benefit[4])
print(Benefit[5])
print(Benefit[6])
print(Benefit[7])

'''
x = np.arange(8)
plt.bar(x, Benefit)
plt.xticks(x, input_year_list)

plt.show()
'''
plt.plot(input_year_list, Benefit)
plt.show()
