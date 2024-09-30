project = int(input("과제 : "))
mid_sub = int(input("중간 : "))
final_sub = int(input("기말 : "))

score = (project + mid_sub + final_sub) / 3

print(f"평균 : {score}")

if score >= 90:
    print("A학점 입니다.")
elif score >= 80:
    print("B학점 입니다.")
elif score >= 70:
    print("C학점 입니다.")
elif score >= 60:
    print("D학점 입니다.")
else:
    print("F학점 입니다.")