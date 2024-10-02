print("별 찍기 \n1.☆ \n2.★ \n3.#")
mod = int(input("모드를 선택 하시오 : "))
count = int(input("길이를 입력 하시오 : "))

if mod == 1:
    shape = "☆"
elif mod == 2:
    shape = "★"
elif mod == 3:
    shape = "#"

if mod == 1:
    for i in range(count):
        if i == 0:
            print(" "*(count*2+2), shape, sep='')
        else:
            print(" "* (count*2+2-i), shape, " "*(i*2-1), shape, sep='')

    print((shape * count), " " * (count * 2 - 1), (shape * count), sep='')

    print(" "* (count-i), shape, " "*(i*5), shape, sep='')

    print(" "* (count-i+2), shape, " "*(i*5-4), shape, sep='')

    print(" "* (count-i+4), shape, " "*(count), shape, " "*(i*2-3), shape, sep='')

    for i in range(count):
        if i <= (count-2):
            print(" "*(count-i-1), shape, " "*(count-i), shape, " "*(i*4-1), shape, " "*(count-i), shape, sep='')
        else:
            print(shape, " "*(count*3+3), shape, sep='')

else:
    for i in range(count):
        if i == 0:
            print(" "*(count*2+1), shape, sep='')
        else:
            print(" "*(count*2+1-i), shape*(i+1), sep='')

    print((shape * ((count * 3)-1)), sep='')

    for i in range(count-2):
        print(" "*(i+1), shape*((count*3)-(i+1)-2), sep='')


    for i in range(count-1):
        if i <= (count-2):
            print(" "*(count-i-1), shape*(count-i-1), " "*(i*5+1), shape*(count-i-1), sep='')
        else:
            print(" ", shape, " "*(count*3+1), shape, sep='')



