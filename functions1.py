def square(number):
    return number * number

def numVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "e" or \
                string[i] == "i" or string[i] == "o" or \
                string[i] == "u":
                    count += 1
    return count

#print("Enter a number: ")
#num = int(input())
#numsquared = square(num)
#print(str(num) + " Squared = " + str(numsquared))
print("Enter a string: ")
sg = input()
print("There are " + str(numVowels(sg)) +  " vowel in the string.")
