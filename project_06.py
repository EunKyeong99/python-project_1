list_a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

list_c = []
count = 1

for i in range(20):
    if count <= len(list_a) or count <= len(list_b):
        for j in range(count):
            if list_a:
                list_c.append(list_a.pop(0))

        for j in range(count):
            if list_b:
                list_c.append(list_b.pop(0))

        count += 1

print(list_c)
