import math

module = 302000000
inverter = 100000000
structure = 539000000
electricity = 120000000
site = 70000000
kepco = 70000000
r = 0.045

construction = (module + inverter + structure + electricity +site)
OM = construction * 0.01

Install = (construction + kepco)

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
        def func_formulaA(input_year):
            sum = 0
            for n in range(0, input_year + 1):
                formulaR = math.pow(1 + r, n)
                sum += (OM / formulaR)
            return sum


        formulaA = func_formulaA(input_year)
        Cost = Install + formulaA
        print("Cost: ", Cost)



        Cost = round(Cost, 2)  # 반올림

        print("Cost:", format(Cost, ','))

        Cost = round(Cost)  # 반올림
        print("(", get_wonwha_string(Cost), ")")

        print("\n\n\n")