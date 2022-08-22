print("1 Unit = 5 ₹")
unit=float(input("Enter the amount of units consumed: "))
price=5*unit
print("Your bill is",price,"₹")
discount=price*10/100
print("Your total bill with added 10% discount is",price-discount)
