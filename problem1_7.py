# %%
def problem1_7():
    b1 = float(input("Enter the length of one of the bases: "))
    b2 = float(input("Enter the length of the other base: "))
    h = float(input("Enter the height: "))
    if b1 == b2:
        A = b1*h
    else:
        A = ((b1+b2)/2)*h
    print("The area of a trapezoid with bases", b1,"and", b2,"and height", h,"is", A)

# %%
