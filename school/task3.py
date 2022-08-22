# Taking input of 3 numbers
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

# Checking whether numbers are equal or not
if a==b==c:
    print("All three numbers are equal.")


else:
    # Storing variable a,b and c in array d
    d=[a,b,c]
    d.sort()
    print("The smallest number is: ",d[0])
    print("The greatest number is: ",d[-1])



