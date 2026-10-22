#ask user for width and loop until they
# enter a number which is more than 0

error = "yo cuh pick a number more than 0\n"
while True:

    try:
        # ask the user for a number
    
        width = float(input("width: "))

        # check that the number is more than 0
        if width > 0:
            break
        else:
            print(error)
    except ValueError:
        print (error)
    
