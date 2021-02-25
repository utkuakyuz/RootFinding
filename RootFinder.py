

def find_roots (a,b,c):  
    """
    This function is a rootfinder for ax^2+bx+c polynomial function. It works for both imaginary roots
    and also real roots. For the algorithm, function uses basic root finding method of mathematics.
    First discriminant value is calculated with b^2-4*c* and then roots are calculated by formula with
    discriminant.
    A loop is used for program to not stop until input is string "Q"
    Parameters
    ----------
    a : String
        This is the coefficient of x^2 of the polynomial function
    b : String
        This is the coefficient of x of the polynomial function
    c : String
        This is the constant number of the polynomial function

    Returns
    -------
       There are 3 different return values. First is for a function which has two roots.
       Second one is for the functions which has coincident roots means only has one root.
       The last one is for imaginary roots and python is showing them with the letter "j". Letter
       "j" implies i in maths which means sqrt(-1). Return values are rounded to 4 digit.

    """
      
    delta = b**2-(4*a*c)
    x1 = (-b-delta**(1/2))/(2*a)
    x2 = (-b+delta**(1/2))/(2*a)
    if delta < 0:
        x1 = round(x1.real,4)+round(x1.imag,4)*1j
        x2 = round(x2.real,4)+round(x2.imag,4)*1j
        return x1, x2
    elif delta == 0:
        x1 = round(x1,4)
        return "There is only one root which is:", x1
    elif delta > 0:
        x1 = round(x1,4)
        x2 = round(x2,4)
        return "There is two instinct roots which are:", x1, x2

while True:
    n1, n2, n3 = input("Enter your coefficients here:").split()
    print(find_roots(int(n1),int(n2),int(n3)))
    stop = input("Enter 'q' for stopping program, if you will continue, press any key:").upper()
    if stop == "Q":
        print("Program Finished")
        break
    else:
        pass
    
    
    
