#ask user for width and loop until they
# enter a number which is more than 0
def num_check(question):

    error = "yo cuh pick a number more than 0\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than 0
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print (error)

 # main routine starts here...   
keep_going = ""
while keep_going == "":

    # get width and height
    width = num_check("width: ")
    height = num_check("height: ")

    # caulculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # dihsplay output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # ask your user if they want to keep going
    keep_going = input ("press enter to keep going or any key to quit.")
    print()

print("thank you for using the area / perimeter caulculator")
