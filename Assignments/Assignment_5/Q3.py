#Question 3 
#Simple number checker function
def check_number(number):
    if number % 2 == 0:  #% gives the remainder; where no remainder means its "even" function
        return "even" 
    else:
        return"odd"


user_number = int(input("Enter a whole number:")) # int() converts the typed text into a whole number



print(f"{user_number} is an {check_number(user_number)} number.")  #outputs if number is "odd" or "even".















        
    
#print(f"enter a number:")
# if (the )

    