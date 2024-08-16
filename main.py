# Import the logo from the art module
from art import logo

# List of alphabet characters, repeated to handle wrap-around in the Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to encode or decode text using the Caesar cipher
def ceaser(start_text, shift_amount, cipher_direction):
    # Initialize the end text variable
    end_text = ""
    # If decoding, reverse the shift amount
    if cipher_direction == "decode":
        shift_amount *= -1
    # Iterate over each character in the start text
    for char in start_text:
        # Check if the character is in the alphabet list
        if char in alphabet:
            # Find the current position of the character
            position = alphabet.index(char)
            # Calculate the new position by applying the shift
            new_position = position + shift_amount
            # Append the shifted character to the end text
            end_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, add it as is
            end_text += char
    # Print the resulting encoded or decoded text
    print(f"Here is the {cipher_direction}d text is {end_text}")


# Print the logo
print(logo)


# Flag to control the continuation of the program
should_continue = True
while should_continue:
    # Ask the user if they want to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Ask the user for the message to encode or decode
    text = input("Type your message:\n").lower()
    # Ask the user for the shift amount
    shift = int(input("Type the shift number:\n"))
    # Ensure the shift amount is within the range of 0-25
    shift = shift % 26
    # Call the Caesar cipher function with the provided inputs
    ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
    # Ask the user if they want to run the program again
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    # If the user types "no", end the program
    if restart == "no":
        should_continue = False
        print("Goodbye")
