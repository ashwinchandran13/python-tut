def tax(amount):
    if amount <= 240:
        return 0
    elif amount > 240 and amount <= 480:
        return amount * .15
    else:
        return amount * .28

def netpay(grosspay):
    return grosspay - tax(grosspay)

#print("Enter amount: ")
#amount = int(input())
#print("The tax amount is " + str(tax(amount)))

print("Enter the grosspay: ")
grosspay = int(input())
print("Gross pay after tax deduction: " + str(netpay(grosspay)))

