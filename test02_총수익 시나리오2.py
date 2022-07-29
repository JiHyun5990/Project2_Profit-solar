import math

PV = 491.4
UR = 0.1666
d = 0.008
r = 0.045

while True:
    input_year = int(input("\n태양광 발전 년수를 입력하세요(종료시 999입력): "))

    if input_year == 999:
        break

    else:
        def func_formulaA(input_year):
            SMP = 100 / 1.02
            REC = 50 / 1.02
            sum = 0
            for n in range(0, input_year + 1):
                formulaD = math.pow(1 - d, n)
                formulaR = math.pow(1 + r, n)
                SMP *= 1.02
                REC *= 1.02
                sum += (UR * formulaD * (SMP + REC) / formulaR)
            return sum


        formulaA = func_formulaA(input_year)

        Benefit = PV * 8760 * formulaA
        print("Benefit: ", Benefit)