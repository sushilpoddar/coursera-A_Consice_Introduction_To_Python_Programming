# %%
import csv

def problem3_7(price,flowername):
    with open(price, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
               if flowername in r:
                   print(r[1])
    pass  # replace this pass (a do-nothing) statement with your code

# %%