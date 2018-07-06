import time
import random

def passcode_generator():
    
    print("<<<random password generator>>>")
    time.sleep(1)
    length = int(input("How long would you like your password to be? >>> "))
    times = int(input("How many passwords would you like? >>> "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passcode = ' '
    amount_of_passwords = (0)

    for x in range(times):
        
        password = ' '
        amount_of_passwords += 1
        
        for i in range(length):
            
            passcode += random.choice(alphabet)
        
           
        print("<<<here is your " + "random password " + str(amount_of_passwords) + " >>>")
        time.sleep(.8)
        
        print(passcode)
        passcode = ' '
        



passcode_generator()
