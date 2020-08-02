def problem3_6(fileName):
    file_n = open(fileName, "r")
    emp = []
    for line in file_n:
        line = line.strip('\n')
        emp.append(line)
        print(len(line))
    f = open('humptylength.txt',"w+")
    for line in emp:
        f.write(str(len(line))+'\n')
