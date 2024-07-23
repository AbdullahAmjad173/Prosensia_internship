rawstr = input("Enter the number")
#use try and except if try works then except will skill and vice versa
try:
 ival = int(rawstr)
 
except:
    ival =-1

if ival > 0:
    print ("Nice work ")
else:
    print("Not a number ")