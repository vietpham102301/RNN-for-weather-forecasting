

with open("data/Origin.csv", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    line = line.replace('\n', '')
    line = line.rstrip(',')
    line += '\n'
    lines[i] = line

with open("data/Data_Weather_processed.csv", "w") as file:
    file.writelines(lines)