#this program show how to reverse a number

import os
os.system("cls")
print("Enter a number:",end="")
num=int(input())
rev=0
while num!=0:
     rev=rev*10+num%10
     num=num//10
print("Reverse of the number is:",rev)