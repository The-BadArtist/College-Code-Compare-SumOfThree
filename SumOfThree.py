'''
A simple program to add three numbers together.
'''
def sum (number1 = 0, number2 = 0, number3 = 0, *args):
    if len(args) > 0: 
        #* Checks if there is any addition variables
        print("Only 3 numbers try again")
    else:
        #Function to add the three parameters
        sum = (number1 + number2 + number3)
        #Prints the output in a regular addition format 
        print(number1, " + ", number2, " + ", number3, " = ", sum) 

    
        
def sum_of_unknown_num( arg = 0, *args):
    sum = arg
    if len(args) > 0:
        for number in args:
            sum += number

    print(sum)


    
if __name__ == "__main__":
    sum(1, 2, 3) # inputs sum(number1 , number2, number3)
    sum_of_unknown_num(1, 3, 5, 6)