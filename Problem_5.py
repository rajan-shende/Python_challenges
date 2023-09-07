# . Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

# Approach 1

colors = ["Red", "Green","White" ,"Black"]
var = len(colors) - 1
print(colors[0], colors[var])

# Approach 2
print(colors[0], colors[-1])