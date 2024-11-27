def infinite_number():
    num = 0
    while True:
        yield num
        num += 1

def echo_coroution():
    while True:
        value = yield
        print(value*2)


gen = infinite_number()
co = echo_coroution()
next(co)

for i in range(11):
    co.send(next(gen))

