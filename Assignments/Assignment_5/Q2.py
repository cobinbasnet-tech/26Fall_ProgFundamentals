#Question 2 
#Rectangle Calculator Function
def rectangle_stats(length, width): # Defining a function that takes length and width
    area = length * width  # finding area
    perimeter = 2 * (length + width) # finding perimeter
    return area, perimeter # Return both values as a pair


# get both length and width from the user and convert it into floating numbers
stats_length =float(input("Enter the length:"))
stats_width =float(input("Enter the width:"))


# call out the function into two separate variables
area, perimeter = rectangle_stats(stats_length, stats_width) 


# print both area and perimeter in 2 decimal points 
print(f"area: {area:.2f}", f"perimeter: {perimeter:.2f}")








#rectangle_stats('stats_length:.2f', 'stats_width:.2f')
#print("stats_length:.2f","stats_width:.2f")


    