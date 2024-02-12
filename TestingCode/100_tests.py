
# guess = 'p'
# chosen_word = 'apple'
# display = []
# for idx in range(0, len(chosen_word)):
#     display.append('_')
# print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# for idx in range(0, len(chosen_word)):
#     if guess == chosen_word[idx]:
#         display[idx] = guess

# print(display)

new_display = ['b', '_', 'a']
c = 0

for item in new_display:
    if '_' in new_display: 
        c += 1

if c > 0:
    print('Guess another letter')
else: 
    print('Word completed')







# Ensure the user's input is a single letter
# if len(guess) == 1 and guess.isalpha(): 
    
#     found_times = 0
#     for letter in chosen_word:
#         if letter == guess:
#             # Count the occurrences of the guessed letter in the chosen word
#             found_times += 1

#     if found_times > 0:
#         print(f"Letter entered '{guess}' appears {found_times}")
#     else:
#         print(f"Letter entered '{guess}' is not in the chosen word")
# else: 
#     print('Enter a single letter, please. Try again')
        





