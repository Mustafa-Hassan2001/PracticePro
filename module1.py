#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dell Latitude E5470
#
# Created:     19/12/2023
# Copyright:   (c) Dell Latitude E5470 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#fname = "Tony"
#lname = "Stark"
#age = 51
#print(fname +"'s age is " + str(age) + " year old")
#print(fname+" is genius")

#superhero = input("what is your superhero name?")
#print(superhero)

#type conversion
#int()
#str()
#float()
#bool()

#age = input("Enter your age: ")
#new_age = int(age) + 5
#print(new_age)

#first = input("Enter 1st number: ")
#secound = input("Enetr 2nd number: ")

#sum = int(first) + int(secound)
#print(sum)
#print("The sum is " + str(num))



#name = "Mustafa Hassan"
#name.upper()


#mystring = "Tnoy Iron"
#print("t" in mystring)


#operators
#print(5+4) #add
#print(7-2)  #sub
#print(3*2) #mul
#print(2/2) #div
#print(4%3)  #mod
#print(2**5) #pow

#print(2>3 or 2<3)
#print(2==2 and 3!=2)
#print(2>=3)
#num1 = input("Enter number-1: ")
#num2 = input("Enter number-2: ")
#opt = input("Enter what you want: /n 1-> ADD /n 2-> SUB /n 3-> MUL /n 4-> DIV /n 5-> MOD")

#if(opt == 1):
 #   sum = num1 + num2
  #  print(sum)
   # break
#elif(opt == 2):
 #   sum = num1 - num2
  #  break
#elif(opt == 3):
 #   sum = num1 * num2
  #  break
#elif(opt == 4):
 #   sum = num1 / num2
  #  break
#elif(opt == 5):
 #   sum = num1 % num2
  #  break
#else:
 #   print("Not Select")


#range
#numbers= range(5)
#print(numbers)

#while-loop

#i=0
#while i<=5:
#    print(i * "*")
#    i=i+1
#i=5
#while i >= 0:
#    print(i * "*")
#    i=i-1

#for i in range(5):
#    print(i+1)


#list  []
#marks = [98, 99, 100]
#print(marks[2])
#print(marks[0:3])

#marks.append(99)
#marks.insert(0, 100)

#print(marks)
#print(99 in marks)
#n = len(marks)
#print(n)
#i=0
#while i < n:
#    print(marks[i])
#    i=i+1
#marks.clear()
#print(marks)

#tuple is just like a list but can't change we can count number of ocures and index number of element ()

#marks = (72, 2, 22, 2, 3)
#print(3 in marks)
# marks[0] = 73 #error beacuse changes not allowed
#print(marks.index(3))
#print(marks.count(2))


#set may only unique element atay hn and index is not exixt here
#marks = {2,3, 4,4}
#print(marks)  #output:

#dictonary may pair ka sat data ata hai
marks = {"sub": 98, "sub2": 88}
print(marks["sub2"])
print(marks)
#add new marks in dictonary
marks["physics"] = 99
print(marks)

#functions
#1)in-build function
#int()
#bool()
#str()

#2) model function
from math import *
print(sqrt(4))

#3)user-define function
def sum(num1, num2):
    print(num1+num2)
sum(3,4)


def mul(num1, num2, num3):
    print(num1*num2*num3)
mul(1, 1, 1)