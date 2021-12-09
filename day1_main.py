# print() -- printing to the output
print("Hello World!")

# string manipulation

# for printing in next line
print("Hello There \nMy name is Aritra")

# string concatenation
print("hello" + "Aritra")

# input function -- take input from user
# input function always stores string in a variable
print("Hello there "+input("What is your name: "))


# coding exercise 1 --
# wap that prints the number of characters in a user's name

user = input("What is your name: ")
print(len(user))

# variables
name = "aritra"
print(name)

# errors --
# we got 3 types of errors so far --
# 1. syntax error - due to wrong syntax name
# 2. indentation error - if we make unnecessary indentations
# 3. name error - undeclared variables called or predefined words are used


# Day 1 project --

print("Welcome user! This is a brand name generator program")

userCity = input("Which city you grew up in:\n")
userPet = input("What is the name of your pet:\n")

print("Your brand name could be - " +userCity+" "+userPet)

# data types --

# strings --
# subscript --
# printing the 2nd character in a string
print("hello"[1])


# type check and type conversion

# type(variable) -- returns the type of the value stored in variable

a = 123
print(type(a))

b = str(a)
print(type(b))

# coding exercise on data types --

num = input("enter a two digit number: ")
print(type(num))

firstDigit = int(num[0])
secondDigit = int(num[1])

print(firstDigit + secondDigit)






