# Specify your filename here
filename = "output.txt"

unique_lines = set()

with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('"bdDn"'):
            unique_lines.add(line)

for line in unique_lines:
    print(line)