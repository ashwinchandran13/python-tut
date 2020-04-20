outFile = open("name.txt",'w')
name = raw_input()
while(name != 'q'):
    outFile.write(name+'\n')
    name = raw_input()
outFile.close()
    
