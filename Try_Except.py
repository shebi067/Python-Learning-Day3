#  Try and Excpet ka concept


try:
 user = int(input("What's Your Age: "))
 print("Your Age:", user, "year")
except:
 print("Please enter only numbers")

try:
 number1 = int(input("Write any number: "))
 print(number1**2)
except:
 print("enter a valid number") 

# little complex task

try:
    num1 = int(input("Enter First Number: "))
    num2 = float(input("Enter the Second Number: "))

    number = num1 / num2
    print("Answer is: ", number)

    if num1<0 and num2<0:
      print("0 or negative number is not acceptable ")
    else:
      number = num1 / num2
    if num1 == "" and num2 == "":
        print ("Enter only number")
    else:
      number = num1 / num2
except:
    print("enter a Valid Number ")


# AI output
try:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter the Second Number: "))

    if num2 == 0:
        print("Error: Please enter a valid number! (don't use 0)")
    else:
        answer = num1 / num2
        print("Answer is:", answer)

except ValueError:

    print("Error: Please enter a valid number!")