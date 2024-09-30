print("별 찍기 \n1.☆ \n2.★ \n3.#")
mod = int(input("모드를 선택 하시오 : "))
count = int(input("길이를 입력 하시오 : "))

if mod == 1:
    shape = "☆"
elif mod == 2:
    shape = "★"
elif mod == 3:
    shape = "#"

for i in range(count):
    if i == 0:
        print(" "*(count*2+2), shape, sep='')
    else:
        print(" "* (count*2+2-i), shape, " "*(i*2-1), shape, sep='')

print((shape * count), " " * (count * 2 - 1), (shape * count), sep='')
