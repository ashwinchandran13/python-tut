#inFile = open('text.txt','r')
#line = inFile.readline()
#while(line):
#    print(line)
#    line = inFile.readline()
#for line in open('text.txt'):
#    print(line)
sum = 0
count = 0
for grade in open('grades.txt'):
    print("grades :" + grade)
    sum = sum + int(grade)
    count = count + 1
average = sum / count
print("Average: " + str(average))
