decision = input("Enter an operation; Addition, Subtraction, Multiplication or Division: ")
var_input = int(input("Enter a number: "))
var2_input = int(input("Enter a number: "))
var_mul = var_input * var2_input
var_div = var_input / var2_input
var_add = var_input + var2_input
var_sub = var_input - var2_input

if decision == "Addition":
    print("The sum is " + str(var_add) + ".")
elif decision == "Subtraction":
    print("The difference is " + str(var_sub) + ".")
elif decision == "Multiplication":
    print("The product is " + str(var_mul) + ".")
elif decision == "Division":
    print("The quotient is " + str(var_div) + ".")

