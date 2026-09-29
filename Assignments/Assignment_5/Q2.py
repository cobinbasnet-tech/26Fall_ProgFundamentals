#Question 2 
#Rectangle Calculator Function
def rectangle_stats(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

stats_length =float(input("Enter the length:"))
stats_width =float(input("Enter the width:"))

area, perimeter = rectangle_stats(stats_length, stats_width)

print(f"area: {area:.2f}", f"perimeter: {perimeter:.2f}")








#rectangle_stats('stats_length:.2f', 'stats_width:.2f')
#print("stats_length:.2f","stats_width:.2f")


    