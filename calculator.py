num_1 = float(input("Enter an integer: "))
op = input("Enter an operator:")
num_2 = float(input("Enter another integer:"))
if op == "+":
    print(num_1 + num_2)
elif op == "*":
    print(num_1 * num_2)
elif op == "-":
    print(num_1 - num_2)
elif op == "/":
    print(num_1 / num_2)
else : 
    print("Invalid Operator.")
 