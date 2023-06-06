#this program illustrate how brackets () and {} are used with conditional statements


a=5
b=6
if {a==5 and b==6}:    #invalid   if {{a==5} and{b==6}} 
    print("yes")
else:
    print("no")

a=1
b=2
if(a==5 and b==2):
    print("yes")
else:
    print("no")
if((a==5) and (b==2)):
    print("yes")
else:
    print("no")

a=7
b=6
if {a==7} and {b==6}:
    print("yes")
else:
    print("no")
if (a==7) and (b==6):
    print("yes")
else:
    print("no")

a=100
b=200
if ({a==100} and {b==200}):
    print("yes")
else:
    print("no")
if {(a==100) and (b==200)}:
    print("yes")
else:
    print("no")