filename = "learning_python.txt"

with open(filename) as fileob:
    line = fileob.read()
    print(line)

with open(filename) as fileob:
    readline = fileob.readlines()

for line in readline:
    print(line.rstrip().replace('Python', 'C'))