#read everything from file
'''with open('file.txt','r') as f:
    content=f.read()
    print(content)'''



#print one by one line from file..........(1)
'''with open('file.txt','r') as f:
    lines=f.readlines()
    print(lines)
    for line in lines:
        print(line)'''




#print one by one line from file..........(2)
with open('file.txt','r') as f:
    for line in f:
        print(line)
