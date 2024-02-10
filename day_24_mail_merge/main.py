# Open the file with names and read each name into a list, stripping newline characters
with open("Input/Names/invited_names.txt") as name_file:
    # List comprehension to strip newline characters from each name
    names = [name.strip() for name in name_file.readlines()]

# Open the template letter and read its content into a variable
with open("Input/Letters/starting_letter.txt") as letter_file:
    # Read the entire content of the letter into a single string
    letter = letter_file.read()

# Loop over each name in the list of names
for name in names:
    # Replace placeholder in the letter template with the actual name
    new_letter = letter.replace("[name]", name)

    # Create a personalized letter file for each name
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as final_letter:
        # Write the personalized letter to the file
        final_letter.write(new_letter)
