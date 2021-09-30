# TASK 1:

# Requirements:
# [1] The function should be named happy_thought and should have no parameters.
# [2] The function should then display the message "What is your happy thought?"
# [3] The function should then read in the user's response.
# [4] The function should then display the message "Think about {thought}." where {thought} is the user's response.
# [5] Finally, the function should display the message "It will help you fly!".


def happy_thought():
    print ("What is your happy thought?")
    thought = input(":")
    print (f'Think about {thought}.')
    print('It will help you fly!')



# TASK 2:

# Requirements:
# [1] The function should be named pixie_dust.
# [2] The function should have 1 parameter named amount which represents the amount of pixie dust that has been used.
# [3] The function should start by checking if the amount is greater than 0.
# [4] The function should display the message "The pixie dust will help you fly!" if the amount is greater than 0.
# [5] Otherwise, the function should display the message "You will need a bit of pixie dust to fly!".



def pixie_dust(amount):
    if amount>0:
        print("The pixie dust will help you fly!")
    else:
        print ("You will need a bit of pixie dust to fly!")



#TASK 3:

# Requirements:
# [1] The function should be named fly.
# [2] The function should have 1 parameter named people which represents the number of people that will fly with Peter Pan.
# [3] For each person in people, the following should be done:
# [4] Display the message "Sprinkling some pixie dust..."
# [5] Finally, the function should display "It is time to fly to Neverland!".



def fly(people):
    for x in range(people):
        print ("Sprinkling some pixie dust...")
    print("It is time to fly to Neverland!")

