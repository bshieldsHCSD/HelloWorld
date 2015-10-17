#I am makign a change to this file

#Sometimes you have to declair your variable to help intellisense
myName = "" 
#Collect Data from the user
myName = input('What is your Name? ')
myName = myName.upper()

#Start of if statment
if myName == 'BRETT':
    print ('Your name is \n'+myName)
    find =  (myName.find('T'))
else:
    print ('Your name is not Brett')

""" myName.find('BRETT')
 myName.replace('BRETT','JOSH')"""



#Prints hello world to the console.
#print('Hello World')


#name = "Brett"[3]
#print (name)


#Basic Input Statement
#nameVar = input("What is your name?:")
#print("Hello "+nameVar)


#Basic if statement
#name = input ("What is your name?")
#if name == 'brett':
#	print('Your Name is Brett')
#else:
#	print('Your name is not Brett')

