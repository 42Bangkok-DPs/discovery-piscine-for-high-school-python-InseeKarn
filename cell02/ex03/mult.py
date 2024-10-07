fn = int(input("Enter first number: "))
sn = int(input("Enter second number; "))

result = fn * sn
print(f"{fn} X {sn} = {result}")

if result > 0:
    print("The result is positive")
elif result < 0:
    print("The result is negative")
else:
    print("The result is positive and negative")
