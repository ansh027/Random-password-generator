import string
import random

## Characters to generate password
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

##defing function
def generate_random_password():

    ##Asking user for length of password
	length = int(input("How long password do you want: "))

	##shuffling the characters
	random.shuffle(characters)
	
	##Picking random characters from the list
	password = []
	for i in range(length):

		password.append(random.choice(characters))
    ##shuffling the resultant password
	random.shuffle(password)
    
    ##converting list to string
    ##printing the password
	print("".join(password))

##executing function
generate_random_password()
