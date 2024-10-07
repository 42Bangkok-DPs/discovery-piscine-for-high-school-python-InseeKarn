number = int(input("Enter a number"))

if number > 25:
    print("ERROR")
while number <= 25:
    print(f"inside the loop, my varible is {number}")
    number += 1
