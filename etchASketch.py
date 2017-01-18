#creating an etchASketch program using turtle
import turtle

#creating variables
penColor = "red"
lineLength = 0
angle = 0

#asking user for input
penColor = input("What pen color would you like to use? ")
lineLength = int(input("How long would you like to make the line? "))
angle = int(input("What angle would you like? "))

#Draw the line as long as the lenght of the given line is not zero
while lineLength != 0:
	turtle.color(penColor)
	turtle.right(angle)
	turtle.forward(lineLength)
#Now ask user again to specify another line and how long. 
	lineLength = int(input("How long would you like to make the line (specify 0 to stop drawing)? "))
#if they enter the lenght to be zero, it is going to print the statement
	if lineLength != 0:
		penColor = input("What pen color would you like to use? ")
		angle = int(input("What angle would you like? "))
print("Great sketch by the way!")

		