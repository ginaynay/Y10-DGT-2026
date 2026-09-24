# Greeting the world
# Nathan Malan
# 23 sept 2026
# version 2


#todo:check and record functions
#    checking for valid awnser
#


#version 1 

'''like_coffee = imput("do you like coffee? ")
#print(like _coffe) # checking the imput is stored
print(f"your awnser was '{like_coffe)}'")

# Ask if they like coffee and respond
if like_coffe == "yes" or like_coffee == "yes" or like_ coffee== "y":
   print("that is great")
   else:
    print("you are missing out! why not give it a try?")'''

#version 2 
#while loop to test the program
keep_going = ""
while keep_going == "": 
    like_coffee = input("Do you like coffee? ")
    #print(like _coffe) # checking the imput is stored
    print(f"your awnser was '{like_coffee}'")

    if like_coffee == "yes" or like_coffee == "yes" or like_coffee == "y" or like_coffee =="y":
        print("that is great")
        keep_going = "Exit"
    elif like_coffee == "NO" or like_coffee == "no" or like_coffee == "N" or  like_coffee == "na":
        print("you are missing out! why not give it a try?")
        Keep_going = "somthing_Else"
    else:
        print("I dont understand. Please try again.")
