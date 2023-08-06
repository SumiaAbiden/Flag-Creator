width = input("Flag width:\n")
width = int(width)
height = input("Flag height:\n")
height = int(height)
# Put the rest of your code here!
upper = int(height/2) * (int(width/2) * "#" + int(width/2) * "-" + "\n")
lower = int(height/2) * (int(width) * "-" + "\n")

print(upper + lower)
