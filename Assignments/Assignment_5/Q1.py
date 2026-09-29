#question 1 
#greeting the user using func. 
def greet_user(name):
    print(f"Hello, {name}! Welcome abroad.") #print greeting using f string to enter name
user_name = input(" Enter your name: ") #ask user to put their name to store it
greet_user(user_name) #call function using the user's name that was stored