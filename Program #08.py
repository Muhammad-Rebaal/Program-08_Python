                                # Quadratic Equation ax**2 + bx + c
                                # a,b,c are real no.
                                # a!=0
                                
import cmath

a = int(input("Input the value of a :"))
b = int(input("Input the value of b :"))
c = int(input("Input the value of c :"))

d = (b**2) - (4*a*c)
root1 = (-b -cmath.sqrt(d))/(2*a)
root2 = (-b +cmath.sqrt(d))/(2*a)

print(f"The roots are {root1} and {root2}")
print("The roots are" ,root1, "and" ,root2)