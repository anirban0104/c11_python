print("Choose any shape: ")
print("Shape selection is case sensitive!")
shape=input("Square/Rectangle/Circle: ")

if shape=="Square":
    print("==User chose the shape square==")
    square_side=int(input("Enter the length of side of square: "))
    print(square_side*square_side)
    print(4*square_side)
if shape=="Rectangle":
    print("==User chose the shape rectangle==")
    l=int(input("Enter the length of rectangle: "))
    b=int(input("Enter the breadth of rectangle: "))
    print(l*b)
    print(2*(l+b))
# now im too lazy to do the circle part, bruhh


