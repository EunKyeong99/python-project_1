def infinite_number():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_number()
for i in range(11):
    print(next(gen))
