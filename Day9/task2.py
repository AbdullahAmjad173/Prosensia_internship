#DEfine function to find the Greater numbers
def filter_values(num , max_num):
    print ("Numbers greater then threshold ")
    #using for loop
    for number in num:
     if number > max_num:
        print (number)
        
    
num = [10,20,30,40,50]
max_num = 10
#function call
filter_values(num,max_num)