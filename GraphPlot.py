# importing the required module
import matplotlib.pyplot as plt
import numpy as np

# x axis values
x = np.arrange(-2*np.pi, 2*np.pi, 0.1)

# corresponding y axis values
y = np.sin((x**2)+x)

# creating z values
z = np.cos(x**2)

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

# plotting the points 
plt.plot(x, z)
  
# naming the x axis
plt.xlabel('x - axis')

# naming the y axis
plt.ylabel('z - axis')
  
# giving a title to my graph
plt.title('Cosine Graph')

# function to show the plot
plt.show()