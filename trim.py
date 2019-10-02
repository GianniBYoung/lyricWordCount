def extraTrim(fileName):
    f = open(fileName, "r")
    text = f.readlines()
    f = open(fileName, "w")

    for line in text:
        if ord(line[0]) != 91 and ord(line[0]) != 40:
            f.write(line)
    f.close()
