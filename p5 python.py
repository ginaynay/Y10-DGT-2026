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
        
# main routine goes here
for item in range(0, 2):
    width = num_check("width: ")
    print(width)

print()

    # main routine goes here
for item in range(0, 2):
    height = num_check("height: ")
    print(height)