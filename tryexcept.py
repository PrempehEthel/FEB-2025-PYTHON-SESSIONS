try:
    file = open("Wexample.txt", "r")
    data = file.read()
    print("The data is: ", data)
except FileNotFoundError:
    print("Sorry, This file does not exist")
finally:
    print("Thank for using me!")
