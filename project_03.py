print("별 찍기 \n1.☆ \n2.★ \n3.#")
mod = int(input("모드를 선택 하시오 : "))

if mod == 1:
    shape = "☆"
elif mod == 2:
    shape = "★"
elif mod == 3:
    shape = "#"
else:
    print("다시 입력하세요")

count = int(input("원하는 크기를 입력하세요 : "))

for i in range(count):
    print(shape, end = " ")