num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
oprators = input("Enter operator (+, %, ^, -, *, /): ")

if oprators == "+":
        result1 = float(num1) + float(num2)
        print(f"Result: {result1}")
elif oprators == "-":
        result2 = float(num1) - float(num2) 
        print(f"Result: {result2}")
elif oprators == "*":
     result3 = float(num1) * float(num2)
     print(f"Result: {result3}")
elif oprators == "/":
        result4 = float(num1) / float(num2)
        print(f"Result: {result4}")
elif oprators == "%":
        result5 = float(num1) % float(num2)
        print(f"Result: {result5}")
elif oprators == "^":
        result6 = float(num1) ** float(num2)
        print(f"Result: {result6}")
else:
        print("Invalid operator")
        result7 = None
        
        #================================================
        
print(int(input("Enter a number: "))+int(input("Enter another number: ")))

#================================================

x = 25.5552
print(round(x, 2)) # rounds x to 2 decimal places
#out = 25.56

#================================================
#formatting numbers with commas
z = 1000
print(f"{z:,}")
