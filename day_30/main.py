try:
    data = open("file.txt")

except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Something")