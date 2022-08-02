import math
import matplotlib.pyplot as plt
import numpy as np

input_year_list = []
Benefit = []
Cost = []

input_year = int(input("\n태양광 발전 년수를 입력하세요: "))
for i in range(0, input_year):
    input_year_list.append(i+1)

SMP = int(input("\n설정하실 초기 SMP 값을 입력하세요: "))
REC = int(input("\n설정하실 초기 REC 값을 입력하세요: "))

SMP_rate = float(input("\n\n설정하실 SMP 증가율을 입력하세요[%]: "))
REC_rate = float(input("\n설정하실 REC 증가율을 입력하세요[%]: "))

#총수익 그래프
PV = 491.4
UR = 0.1666
d = 0.008
r = 0.045

for i in input_year_list:
    def func_formulaA(input_year):
        SMP = 100 / (1 + SMP_rate / 100)
        REC = 50 / (1 + SMP_rate / 100)
        sum = 0
        for n in range(0, input_year + 1):
            formulaD = math.pow(1 - d, n)
            formulaR = math.pow(1 + r, n)
            SMP *= (1 + SMP_rate / 100)
            REC *= (1 + SMP_rate / 100)
            sum += (UR * formulaD * (SMP + REC) / formulaR)
        return sum

    formulaA = func_formulaA(i)
    Result1 = PV * 8760 * formulaA
    Benefit.append(Result1/10000000)

plt.bar(input_year_list, Benefit, label='Benefit', color='lightskyblue')


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
    Cost.append(Result2/10000000)

plt.plot(input_year_list, Cost, label='Cost', color='blueviolet')


#두 그래프의 교차점
intersections = []
prev_dif = 0
x0, prev_c1, prev_c2 = None, None, None
for x1, c1, c2 in zip(input_year_list, Benefit, Cost):
    new_dif = c2 - c1
    if np.abs(new_dif) < 1e-12:
        intersections.append(x1, c1)
    elif new_dif * prev_dif < 0:
        denom = prev_dif - new_dif
        intersections.append(((-new_dif*x0  + prev_dif*x1) / denom, (c1*prev_c2 - c2*prev_c1) / denom))
    x0, prev_c1, prev_c2, prev_dif = x1, c1, c2, new_dif


#그래프 그리기
plt.legend()
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Profit-solar')
plt.text(27, 195, 'unit: 10,000,000', fontsize = 11,
         bbox=dict(boxstyle='square', color = 'azure'))
plt.plot(*zip(*intersections), marker='o',
         markerfacecolor='tomato', markeredgecolor='tomato',
         alpha=1, ms=8)
plt.annotate('Payback Period', xy=intersections[0],
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc3, rad=-.2',
                             color='tomato'),
             xytext=(10, 155), color='tomato')
plt.show()