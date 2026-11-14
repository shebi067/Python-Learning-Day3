
Names = "bwp",'mux',"lhr","isb","khi"

print(len(Names))

inte= 1,3,4,

Name = "Bahawalpur is a Great City"

print(Name[0:18])

print(Name.upper())
print(Name.lower())
print(Name.split())
print(Name.strip())

Naam = "ALi"
Age = 19


txt = f"My name is {Naam} and my age is {Age}" 
print(txt)

print (f"My name is {Naam} and my age is {Age}")

txt2= f"The five dollar price is {5*280} in pKr"
print(txt2)

# String Methods

txt3 = "rUssia"

x = txt3.capitalize() #Captilize the first letter of a string
print(x)

x1 = txt3.casefold() # it smalls all latter of string
print(x1)

x2 = txt3.center(20) #use for center the word by using sapce (! it only work for 1 word)
print(x2)

x3 = txt3.count("rUssia") # it count how many time string appeared
print(x3)

x4 = txt3.encode() # Returns an encoded version of the string
print(x4)

x5 = txt3.endswith("i") # it check the end leeter of string, if yes it says true otherwise false
print(x5)

x6 = txt3.expandtabs(4) #Sets the tab size of the string
print(x6)

x7= txt3.find("s") # it findouts the value of given string
print(x7)

x8 = {"name": "Ali", "city": "Lahore"} #Formats specified values in a string
print("Hello {name} from {city}".format(**x8))
print("Hello {name} from {city}".format_map(x8))

x9 = txt3.index("i") # it also find index value of string
print(x9)

# join 

Php = ["Html", "Css", "Js"]
print(Php)
print(" ".join(Php))# converting list into string

print("-".join(Php))# converting list into url slug format

php = "HTML,CSS,JS"  # converting string into a lsit 
pHp = php.split(",")
print(pHp)


Name1 = Name.find("Great") # finding the index of starting word in string
print(Name1)

Name2= Name.find("java") # output: is -1.  it means that the word is not existing
print(Name2)

Name3= Name.count("a") # it tells how many a character is appeared in string
print(Name3)

#billing

Order = "Air Conditioner"
Quantity = 2
Recipt = "I odered {}  piece of {}"
print (Recipt.format(Quantity, Order))