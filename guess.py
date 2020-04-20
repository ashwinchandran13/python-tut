answer = "Watson"
tr = 3
print("Guessing Game ")
print("What is the name of that guy? ")
response = raw_input()
if response == answer:
    print("Thats right ! ")
else:
    print("Sorry.Guess again " + str(tr-1) + "guesses remaining")
    response = raw_input()
    if response == answer:
        print("Thats right ")
    else:
        print("Sorry, Guess again " + str(tr-2) + "guesses remaining")
        response = raw_input()
        if response == answer:
            print("Thats right")
        else:
            print("Sorry " + str(tr-3) + "guesses remaining")
            print("The answer is " + answer + ".")
