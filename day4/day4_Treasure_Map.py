line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position = input("Enter the position (e.g., A1): ")  # Where do you want to put the treasure?

# Check if input is valid
if len(position) != 2 or position[0] not in "ABC" or position[1] not in "123":
    print("Invalid input. Please enter a letter (A-C) followed by a number (1-3).")
else:
    # Convert input to indices
    column = ord(position[0].upper()) - ord('A')  # Convert 'A', 'B', 'C' to 0, 1, 2
    row = int(position[1]) - 1  # Convert '1', '2', '3' to 0, 1, 2

    # Place the treasure
    map[row][column] = "X"

    # Print the updated map
    print(f"{line1}\n{line2}\n{line3}")
