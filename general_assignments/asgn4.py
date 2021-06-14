'''Excercises related to String'''

x=str(input('Enter the one string = '))
y=str(input('Enter the 2nd string = '))

print(x+'\t'+y)#+ operator is used for concatenation

print(3*x+2*y) 
'''the * this operator printed string
					gives no. of times''' 

print('Ra' 'hul')
print('II' 'CMR')
'''in above the two string literals are enclosed in quotes
which are connect(concatenated) to each other 
note= this is works with only string literals not
with words not with variables'''

x='rah'
y='hul'
print(x+y) # this will give error we are not treated
		   #it as above u want to continue this code
		   #then write + operator between x and y

word="Rahul Bantode"
z=word[1]

print(z)

#string are subscripted which index start with 0 

print(len(word)) #for knowing the length of string

print(word[2:5]) #its the syntax of slice the string
				#into substring

print(word[:])#this will return exact same string as
			  #original string

print(word[:4])#here we not pass from where it to start
			   #slice then it will consider it from 1st

print(word[6:])	# it print forn no. 6 index

#word[3]='j'
#this will give an error because string is mutable type
#we are not allowed to change it	   



