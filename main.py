import random  
import string
import time
print ("What Is The Password That We Will try to Find?\n" "No Special Charcters")
x=input("")
guess = ""
tries = 0
attempts = []
def specific_string(length):  
    sample_string = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890' # define the specific letters it comes from
    # define the condition for random string  
    global result
    result = ''.join((random.choice(sample_string)) for x in range(length))
start = time.time()
while guess != x:
    specific_string(len(x))
    tries += 1
    guess = result
    if guess != x:
        attempts.append(guess)
end = time.time()
final = end - start
final = str(final)
print(attempts)
tries = str(tries)
print(tries + " Tries")
print("Your Password was " + result)
print("It Took " + final + " Secconds")
    
