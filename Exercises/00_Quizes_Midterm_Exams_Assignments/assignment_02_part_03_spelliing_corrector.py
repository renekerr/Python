"""
Part 3: Spelling corrector

Write a function named spelling_corrector that accepts two arguments. The first argument is a sentence (string) and the
second argument is a list of words (correct_spells). Your function should check each word in the input string against
all the words in the correct_spells list and return a string such that:

* If a word in the original sentence matches exactly with a word in the correct_spells then the word is not modified
and it should be directly copied to the output string.

* If a word in the sentence can match a word in the correct_spells list by replacing, inserting, or deleting a single
character, then that word should be replaced by the correct word in the correct_spelled list.

* If neither of the two previous conditions is true, then the word in the original string should not be modified and
should be directly copied to the output string.



Notes:
-Do not spell check one or two letter words (copy them directly to the output string, i.e: a, is, an, or, in)
-In case of a tie use the first word from the correct_spelled list.
-Ignore capitalization, i.e. consider capital letters to be the same as lower case letters.
-All characters in the output string should all be in lower case letters.
-Assume that the input string only includes alphabetic characters and spaces. (a-z and A-Z)
-Remove extra spaces between the words.
-Remove spaces at the start and end of the output string.

Examples:


Sentence (str)	            correct_spells (list)	                        Function return (str)
¨¨¨¨¨¨¨¨¨¨¨¨¨¨              ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨                           ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
Thes is the Firs cas	    ['that','first','case','car']	                thes is the first case
programing is fan and eesy	['programming','this','fun','easy','book' ]	    programming is fun and easy
Thes is vary essy	        ['this', 'is', 'very', 'very', 'easy']	        this is very easy
Wee lpve Pythen	            ['we', 'Live', 'In', 'Python']	                we live python

Notice:
In the first example 'thes' is not replaced with anything.

In the first example both 'case' and 'car' could replace the 'cas' in the original sentence, but 'case' is
selected because it was encountered first.

Please notice that this assignment is only an exercise and a real spell checker requires more functionalities.

Hint: You should use the functions that you developed in part 1 and part 2 to help you solve this problem.

"""


#### Define Function(s) ####

def spelling_corrector (s,correct_spelled):
    words = s.strip().split()   # Remove leading/trailing (strip) spaces and converting sentence to list (split)
    output_str = ''             # Set an empty string

    for current_word in words:  # Loop through elements/words in the sentence (converted to list)
        # If the length of the word is equal to 2 (or less) OR that word is in 'correct_spelled' list
        # then add it to the output string separated by a space


        if len(current_word)<=2 or (current_word in correct_spelled) :

            output_str = output_str + ' ' + current_word

            continue  # It skips the rest of the code inside the loop for the current iteration only
                      # Loop does not terminate but it continues on with the next iteration

        replacement_word = current_word

        # Next iteration loops through each element in 'correct_spelled' list so as to compare current word with
        # each element in it.

        # We call previous functions (find_mismatch and single_insert_delete) within the min() function
        # If the result is equal to 1 that means:

        #       Find Mismatch
        #       if the two strings have the same length and mismatch in only one character.

        #       Find single insertion or deletion
        #       if the first string can become the same as the second string by inserting or deleting a single
        #       character. Notice that inserting and deleting a character is not the same as replacing a character.

        # Then, we assign variable replacement_word the value of correct_word

        for correct_word in correct_spelled:
            #test1 = _find_mismatch(current_word,correct_word)
            #test2 = _single_insert_or_delete(current_word,correct_word)
            #print(current_word, correct_word)
            #print(test1, test2)
            if min(_find_mismatch(current_word,correct_word), _single_insert_or_delete(current_word,correct_word))==1:

                replacement_word = correct_word
                break       # This break statement terminates the loop containing it
                            # The program jumps to the statement immediately after the body of the loop

        output_str = output_str + ' ' + replacement_word

    return output_str.strip().lower()



def _find_mismatch(s1,s2):
    if len(s1) != len(s2):
        return 2
    s1=s1.lower()
    s2=s2.lower()
    number_of_mismatches=0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            number_of_mismatches=number_of_mismatches+1
            if number_of_mismatches>1:
                return 2
    return number_of_mismatches





def _single_insert_or_delete(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if s1==s2:
        return 0
    if abs(len(s1)-len(s2))!=1:
        return 2

    if len(s1)>len(s2):
        # only deletion is possible
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 2
        return 1
    else: # s1 is shorter Only insertion is possible
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 1
                else:
                    return 2
        return 1




#### Main Program ####

sentence = 'Thes is the Firs cas'
correct_spelled = ['that','first','case','car']
#print(sentence)
#print(correct_spelled)
#print('\n')
fn = spelling_corrector(sentence, correct_spelled)
print(fn)
