#numbers = range(1,11)
#it = iter(numbers)
#print(it.next())
import os
files = os.popen('python')
fileIt = iter(files)
print(fileIt.next())
print(fileIt.next())
print(fileIt.next())
#for file in files:
#    print(file)


