number = int(input("Enter a number to see its multiplication table: "))

for x in range(0, 10):
    x = x + 1 
    result = number * x
    print(number, "*", x, "=", result)
