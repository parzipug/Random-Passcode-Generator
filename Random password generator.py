import time
import random

def whitespace(x):
    
    for i in range(x):
        print("\n")
        

def normalspace(x):

    for i in range(x):
        whitespace(1)
        time.sleep(.8)
        

def passcode_generator():
    
    print("<<< Random password generator. >>>")
    normalspace(1)
    
    length = int(input("How long would you like your password to be? >>> "))
    normalspace(1)
    
    times = int(input("How many passwords would you like? >>> "))
    normalspace(1)
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passcode = ' '
    amount_of_passwords = (0)

    for x in range(times):
        
        password = ' '
        amount_of_passwords += 1
        
        for i in range(length):
            
            passcode += random.choice(alphabet)
        
           
        print("<<< Here is your " + "random password " + str(amount_of_passwords) + ". >>>")
        
        print(passcode)
        passcode = ' '
        



passcode_generator()
