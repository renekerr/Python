alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shift = 9
alphabet_shifted = alphabet[shift:] + alphabet[:shift]

text = 'zulu'
cipher_text = ''

for i in text:
    k = alphabet.index(i) #using letter to get index in alphabet list
    cipher_text += alphabet_shifted[k]
    #print(f"{i} on  alphabet index is {k}\t|\tvalue of index {k} on alphabet_shifted is {alphabet_shifted[k]}")

print(f"The encoded text is {cipher_text}")




'''
print(alphabet)
print(alphabet_shifted)


['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']



# for i, elem in enumerate(text):
#     k = alphabet.index(elem)
#     cipher_text += alphabet_shifted[k]

'''