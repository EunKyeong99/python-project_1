print("별 찍기 \n1.☆ \n2.★ \n3.#")
mod = int(input("모드를 선택 하시오 : "))
count = int(input("길이를 입력 하시오 : "))

if mod == 1:
    shape = '☆'
elif mod == 2:
    shape = '★'
else:
    shape = '#'

rows = 5 if count % 2 == 1 else 6

for i in range(rows):
    if i == 0:
        print("    " + shape + "    " + shape)
    elif i == 1:
        print(shape * 10)
    elif i == 2:
        print("  " + shape + "   " + shape + "  ")
    elif i == 3:
        if rows == 6:
            print("  " + shape + "   " + shape + "   ")
        else:
            print(shape * 10)
    elif i == 4:
        if rows == 6:
            print(shape * 10)
        else:
            print(shape + "    " + shape + "    ")
    elif i == 5:
        print(shape + "    " + shape + "    ")