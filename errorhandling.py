try:
    #x = 10/0 
    num = int(input("Enter a number: "))
    print(num)

except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")