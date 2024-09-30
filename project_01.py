weight = int(input("몸무게를 입력해주세요 : "))
height = float(input("자신의 키를 입력해주세요 : "))

bmi = weight / (height ** 2)

print(f"BMI 지수 : {bmi}")