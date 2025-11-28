#PAUSE 1 - Review
def greet():
    print("Hello")
    print("how do you do?")
    print("Isn't the weather nice?")

greet()

#Functions that allow inputs
def greet_with_name(name):
    print(f"Hello, {name}!")
    print(f"how do you do {name}?")

greet_with_name("shashank")

#PAUSE 1 - positional arguments
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}!")

greet_with(name="Shaw", location="Chicago")

#Ceasar Cipher - 1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    display = ""
    for char in original_text:
        display += alphabet[(alphabet.index(char) + shift_amount) % len(alphabet)]
    print(display)

encrypt(text, shift)

#Ceasar Cipher - 2
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#     original_text = ""
#     for letter in cipher_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         original_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {original_text}")

def caesar(original_text=text, shift_amount=shift, encode_or_decode=direction):
    cipher_text = ""
    for letter in original_text:
        if encode_or_decode == "encode":
            shifted_position = alphabet.index(letter) + shift_amount
        else:
            shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")

caesar(text, shift, direction)