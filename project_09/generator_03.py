def read_lines(python):
    with open(python) as f:
        for line in f:
            yield line.strip()

def uppercase_transformer(lines):
    for line in lines:
        yield line.upper()

file_path = 'python.txt'

lines = read_lines(file_path)
result = uppercase_transformer(lines)

for line in result:
    print(line)
