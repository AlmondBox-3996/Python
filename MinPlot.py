# importing the required module
import matplotlib.pyplot as plt
import numpy as np
  
# x axis values
x = np.arrange(-15,15,1)

# corresponding y axis values
y = (3*(x**2))+(8*(np.sin(x)))

# creating list of points
l = []

# inserting values into list
for i in range(-15,16):
    l = l.append(3*(i**2))+(8*(np.sin(i)))

# outputing minimum element
print(min(l))

# plotting the points 
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')

# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('Sine Graph')
  
# function to show the plot
plt.show()