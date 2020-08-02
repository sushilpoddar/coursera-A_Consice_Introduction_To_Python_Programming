# %%
def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a = float(input("Enter length of side one: "))
    b = float(input("Enter length of side two: "))
    c = float(input("Enter length of side three: "))
    s = (a + b + c)/2
    areas = s*((s-a)*(s-b)*(s-c))
    print("Area of a triangle with sides", a, b, c, "is", areas ** 0.5)
# %%