# %%
def problem3_1(fileName):
    file_n = open(fileName, "r")
    count = 0
    for line in file_n:
        count += len(line)
        print(line, end='')
    for line in file_n:
        count += len(line)
    print("")
    print('\nThere are '+str(count)+ ' letters in the file.')
    pass  # replace this pass (a do-nothing) statement with your code

# %%
