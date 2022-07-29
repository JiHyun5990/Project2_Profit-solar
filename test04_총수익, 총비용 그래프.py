import math
import matplotlib.pyplot as plt

input_year_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                   21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                   31, 32, 33, 34, 35]
Benefit = []
Cost = []


#총수익 그래프
PV = 491.4
UR = 0.1666
d = 0.008
SMP = 100
REC = 50
r = 0.045

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
    Result1 = PV * 8760 * formulaA
    Benefit.append(Result1/100000)

plt.bar(input_year_list, Benefit, label='Benefit', color='limegreen')

'''
x = np.arange(35)
plt.bar(x, Benefit)
plt.xticks(x, input_year_list)
'''


#총비용 그래프
module = 302000000
inverter = 100000000
structure = 539000000
electricity = 120000000
site = 70000000
kepco = 70000000
r = 0.045

construction = (module + inverter + structure + electricity + site)
OM = construction * 0.01

Install = (construction + kepco)

for i in input_year_list:
    def func_formulaA(input_year):
        sum = 0
        for n in range(0, input_year + 1):
            formulaR = math.pow(1 + r, n)
            sum += (OM / formulaR)
        return sum

    formulaA = func_formulaA(i)
    Result2 = Install + formulaA
    Cost.append(Result2/100000)

plt.plot(input_year_list, Cost, label='Cost', color='violet')

#그래프
plt.legend()
plt.show()
