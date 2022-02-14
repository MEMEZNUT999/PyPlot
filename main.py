

# importing the required module
import matplotlib.pyplot as plt
from time import sleep


# Intro

print("Automatic Graph Drawer v0.1\n")
#Options start
x1 = int(input("X-axis 1st point: "))
x2 = int(input("\nX-axis 2nd point: "))
x3 = int(input("\nX-axis 3rd point: "))

y1 = int(input("\nY-axis 1st point: "))
y2 = int(input("\nY-axis 2nd point: "))
y3 = int(input("\nY-axis 3rd point: "))
print("\nTip: You can add/remove points, but you will have to edit the code")
sleep(1)
print("\nWARNING! IF YOU PLOT A NUMBER LOWER THAN THE MINIMUM RANGE IT WILL NOT WORK!\n")

XLS = int(input("\nX-axis minimum range: "))
XLM = int(input("\nX-axis maximum range: "))

YLS = int(input("\nY-axis minimum range: "))
YLM = int(input("\nX-axis maximum range: "))
sleep(1)
titl = input("\nGraph title: ")
xla = input("X-axis name: ")
yla = input("Y-axis name: ")
# Options end
print("\n\n Generating results....")
sleep(3)
 
# x axis values ( You can add x4, x5, x6, etc.), but make sure you also create an input (see above!)
x = [x1,x2,x3]
# corresponding y axis values (esit it the same as x axis)
y = [y1,y2,y3]
 
 # setting x and y axis range
plt.ylim(YLS,YLM)
plt.xlim(XLS, XLM)
 
#v plt.set_ylim(bottom=0)
 
# plotting the points
plt.plot(x, y, color='red', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6)
 
# naming the x axis
plt.xlabel(xla)
# naming the y axis
plt.ylabel(yla)
 
# giving a title to my graph
plt.title(titl)
 
# function to show the plot
plt.show()