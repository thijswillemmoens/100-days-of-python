alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):

	original_word = original_text
	decrypted_list = []

	# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
	#  by the shift amount and print the encrypted text.
	for letter in original_word:

		# assign every character to a variable
		position = alphabet.index(letter)

		# change the position in alphabet
		new_position = position + shift_amount

		# assign new character to list
		decrypted_list.append(alphabet[new_position])

	# Make a string of the list of words
	decrypted_word = "".join(decrypted_list)

	# Output new word to console
	print(decrypted_word)
	

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt("hello", 3)