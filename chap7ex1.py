tries = 0
answer = "Watson"
while(tries<3):
    print("Wht is the answer?")
    response = raw_input()
    tries = tries + 1
    if (response == "Watson"):
        print("That is right")
        break
    elif(tries == 3):
        print("Sorry, the answer is Watson")
    else:
        print("Sorry, Try again")

