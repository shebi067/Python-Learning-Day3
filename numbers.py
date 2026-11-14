#numbers

number = 8-2
print (number)

numbers = 9-8*2*(9-1)
print (numbers) 

inte = 49//7
print(inte)

intee = 92**3
print (intee)

#boolean

maker =  True + True
print (maker)

makers = True -(True+ False+False)
print (makers)


age = 21
if age>= 21:
    print("You are an adult")
else:
    print("You are underage")

age >= 18 

#random functions
import random
Integers = [1,3,5,2,7,3,9,23,54,76]
Int = random.choice(Integers)
print(Int)

INT = random.randint(1,20)
print(INT) 

cards = ["Diamond","Heart","Spade","King"]
random.shuffle(cards)
print(cards)




rand= random.randint(1,4)
print(rand)

#sets

a={1,2,3,4,8}
b= {2,1,4,5,9,11}
c={7,6,4,3,20,21,43,54}
d = {21,4,5,65,34,64,54,34,43,42}
print(a&b)

print(a^b)

print (a|b^c)

print (a|b^c&d)

