#add from main import findpass in the beging of your other file for it to work
#Then do findpass("a") with a being your password or you can substitute it out
import random  
import string
import time
def findpass(pas):
    print ("What Is The Password That We Will try to Find?\n" "No Special Charcters")
    guess = ""
    tries = 0
    attempts = []
    #Random String Generaotr
    def specific_string(length):  
        sample_string = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890' # define the specific string  
        # define the condition for random string  
        global result
        result = ''.join((random.choice(sample_string)) for x in range(length))
    start = time.time()
    #Checks If THe Pass Is Correct
    while guess != pas:
        specific_string(len(pas))
        tries += 1
        guess = result
        if guess != pas:
            attempts.append(guess)
    end = time.time()
    final = end - start
    final = str(final)
    print(attempts)
    tries = str(tries)
    print(tries + " Tries")
    print("Your Password was " + result)
    print("It Took " + final + " Secconds")
#This is where you put the passowrd
findpass("ad")
        
