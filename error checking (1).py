
# Online Python - IDE, Editor, Compiler, Interpreter

# Error checking
# Juergen Lier
# 14 October 2026

# Code that tests whether a valid input was given (v1)
'''done = True # Boolean variable set to True
while done:
    num = int(input("Please enter your value as an integer: "))
    done = False

print(f"The number you entered is {num}")'''

# Using a try and except method to check for valid input (V1.1)
# Use try and except method to catch errors
'''done = False
while not done:
    try: # This method tries for a valid input
        num = float(input("Please enter a number: "))
        done = True

    except ValueError:
        print("That is not a valid float number. \nUse a fullstop as decimal indicator. \n ")

print(f"The number you entered is {num}.")'''

# Check for valid input and recyling code with a function (V1.2)
# Create a function to call every time I ask the user
# for a number. A function is a chunk of code that does
# something.
# Functions can be used over and over again.
# To use a function (call it), write out its name with
# parenthesis at the end.
# To create a function, start with the word def
'''def input_check():
    while True:
        try:
            num = float(input("Please enter a number: "))
            break
        except ValueError:
            print("That is not a valid float number.\n")

    print(f"The number you entered is {num}")

# Main routine
input_check() #This call the function to be used.'''
'''
# V1.3 Valid input checker
# Use parameters in the function
# More Pythonic
def input_check(question): # 'question' is a placeholder
    while True:
        error = " gang that aint a valid number."
        print(question)
        try:
            num = float(input())
            break
        except ValueError:
            print(error)

    return(num) # Gives back the value of num
                # so that I can use it outside of
                # the function.

# Main routine
num1 = input_check("Please enter your first number:")
print(f"The number you stored is {num1}")

num2 = input_check("Please enter the second number:")
print(f"The second number you stored is {num2}")

sum = num1 + num2
print(f"Your numbers added added result in {sum}.")
'''
def valid_num(question, low, high):
    error = f"na uh, that is not an inager between {low} and {high}."
    while True:
            try:
                response = int(input(question))
                # if the response >= to the low nr or <= high nr, than continue
                if low <= response <= high:
                    break # stop the loop
                
                else:
                    print(error)
                    
            except ValueError:
              print(error)
    return response # this makes the response available to be used outside the function
    
    # Main routine
if __name__=="__main__":
    
    num1 = valid_num("enter a number between 1 and 10: ",1,10)
    print(f"the number you entered is {num1}. \n")
    
    num2 = valid_num("enter a number between 15 and 20",15, 20)
    print(f"the number you entered is {num2}. \n")
    
    num3 = valid_num("enter a number between 70 and 90",70,90)
    print(f"the number you entered is {num3}. \n")
    
    #multipy the result of num1 num2 num3
    multiply = num1 * num2 * num3
    print(f"Your numbers multiplied are {multiply}")
