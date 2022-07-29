import math

PV = 491.4
UR = 0.1666
d = 0.008
r = 0.045


def get_wonwha_string(num_wonwha_amout):
    str_result = ""
    str_sign = ""
    num_change = num_wonwha_amout

    if num_change == 0:
        str_result = "0"
    elif num_change < 0:
        str_sign = "-"
        num_change = abs(num_change)

    if num_change >= 100000000:
        str_result += f"{int(num_change // 100000000):,}억"
        num_change = num_change % 100000000
    if num_change >= 10000:
        str_result += f" {int(num_change // 10000):,}만"
        num_change = num_change % 10000
    if num_change >= 1:
        str_result += f" {int(num_change):,}"

    str_result = str_result.strip()
    if len(str_result) >= 1:
        return str_sign + str_result + "원"
    else:
        return str_result


while True:
    input_year = int(input("\n태양광 발전 년수를 입력하세요(종료시 999입력): "))

    if input_year == 999:
        break

    else:
        print("\n초기 SMP 설정: 100\n")
        print("초기 REC 설정: 50\n")
        print("======================")
        SMP_rate = float(input("\nSMP의 증가율을 입력하세요[%]: "))
        REC_rate = float(input("\nREC의 증가율을 입력하세요[%]: "))


        def func_formulaA(input_year):
            SMP = 100 / (1 + SMP_rate/100)
            REC = 50 / (1 + SMP_rate/100)
            sum = 0

            for n in range(0, input_year+1):
                formulaD = math.pow(1 - d, n)
                formulaR = math.pow(1 + r, n)
                SMP *= (1 + SMP_rate/100)
                REC *= (1 + SMP_rate/100)
                sum += (UR * formulaD * (SMP + REC) / formulaR)
            return sum

        formulaA = func_formulaA(input_year)
        Benefit = PV * 8760 * formulaA

        Benefit = round(Benefit, 2) #반올림

        print("Benefit:", format(Benefit, ','))

        Benefit = round(Benefit)  # 반올림
        print("(", get_wonwha_string(Benefit), ")")


        print("\n\n\n")
