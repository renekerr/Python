# Step 1
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

# Step 2
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# Step 3
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# Step 4
#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 


from art import logo

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
running = True

def caesar(text, shift_amount, direction):
    shifted_letters = letters[shift_amount % 26:] + letters[:shift_amount % 26]  # Handle shifts beyond 26
    encrypted_text = ""

    for char in text:
        if char in letters:
            if direction == "encode":
                new_index = letters.index(char)
                encrypted_text += shifted_letters[new_index]
            elif direction == "decode":
                new_index = shifted_letters.index(char)
                encrypted_text += letters[new_index]
            else:
                encrypted_text += char  # Handle non-alphabetic characters

    print(f"The {direction}d text is: '{encrypted_text}'")


while running:
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message, shift, action)

    choice = input("Run again? Type 'yes' or 'no':\n").lower()
    if choice != "yes":
        running = False
        print("Goodbye")



    







# caesar_cipher('khoor', 3, 'decode')



# Teacher's approach
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
'''




# Encrypt and decrypt functions separatedly
'''
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shifted_alphabet = alphabet[shift:] + alphabet[:shift]

def encrypt(plain_text, shift_amount):
    cipher_text = ''
    
    for i in text:
        k = alphabet.index(i) #using letter to get index in alphabet list
        cipher_text += shifted_alphabet[k]
        #print(f"{i} on  alphabet index is {k}\t|\tvalue of index {k} on shifted_alphabet is {shifted_alphabet[k]}")

    print(f"The encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
    cipher_text = ''

    for i in text:
        k = shifted_alphabet.index(i) #using letter to get index in alphabet list
        cipher_text += alphabet[k]
        #print(f"{i} on  alphabet index is {k}\t|\tvalue of index {k} on shifted_alphabet is {shifted_alphabet[k]}")

    print(f"The decoded text is {cipher_text}")

if direction == 'encode':
    encrypt(plain_text = text, shift_amount = shift)
elif direction == 'decode':
    decrypt(plain_text = text, shift_amount = shift)
'''




