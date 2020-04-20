#word = "hello"
#for letter in word:
#    print(letter)
sentence = "now is the time for all good people to come to the aid"
count = 0
count1 = 0
for letter in sentence:
    count1 = count1 +1
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' \
            or letter == 'u':
                count = count +1
print('Total no. of letters is ' + str(count1) +'\n' +' The no. of vowels is ' + str(count) + ' ' + 'and the no. of consonants is ' + str(count1 -count))

