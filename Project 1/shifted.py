#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:18:21 2024

@author: Aidan Alme
@JHED: aalme2
"""

# The number of characters in the sample text
num_chars = 0

# A list to store the character frequency probabilities to be used later
char_probabilities = [0]
char_probabilities = [0] * 26

# Open file titled sample.txt
my_sample_file = open('pride_prejudice.txt', 'r', encoding='utf-8-sig')

# Iterate through each line in file my_sample_file
for line in my_sample_file:
    for char in line:
        # Counts how often eletters from a to z occur, converts to lowercase
        if ord(char.lower()) >= 97 and ord(char.lower()) <= 122:
            char_probabilities[ord(char.lower()) - 97] += 1
            # Counts the total number of characters
            num_chars += 1 

# Divides each count by the total number of characters to find the probability            
for index, num in enumerate(char_probabilities, start = 0):
    char_probabilities[index] = char_probabilities[index] / num_chars            
            
# Close the file
my_sample_file.close()

# Prompts the user for the encrypted message
encrypted_message = input("Enter the encrypted message: ")

# A list to store the decryption possibilities
decrypted_messages = []

# The total number of valid letters (the same in each "decryption")
num_letters = 0

# "Deciphers" the message with each possible key value
for num in range(1, 26, 1):
    num_letters = 0
    decrypted_messages.append("")
    for char in encrypted_message:
        if ord(char) >= 97 and ord(char) <= 122:
            # Shifts the characters using their ASCII values
            char = chr((((ord(char) - 97)) + num) % 26 + 97)
            # Counts the number of letters
            num_letters += 1
        decrypted_messages[num - 1] += char    

# A list of lists to keep track the character counts in each "decipherment"    
message_char_frequencies = []

# Counts the appearance of each character in each "decryption"
for index, message in enumerate(decrypted_messages, start = 0):
    message_char_frequencies.append([0] * 26)
    for char in decrypted_messages[index]:
        if ord(char) >= 97 and ord(char) <= 122:
            message_char_frequencies[index][ord(char) - 97] += 1

# A list to store the chi score for each "decipherment"            
chi_scores = []

# The lowest chi score, starts at the maximum
lowest_score = float('inf')

# The index of the most likely decryption
lowest_score_index = 26

# Calculates the chi score for each "decryption"
for index, message in enumerate(decrypted_messages):
    chi_scores.append(0)
    # Iterates throught the list of counts
    for char, num in enumerate(message_char_frequencies[index]):
        chi_scores[index] += (((num - (char_probabilities[char] * 
                              num_letters)) ** 2) / (
                              char_probabilities[char] * 
                              num_letters))
    # Tracks the smallest chi score and its index                              
    if chi_scores[index] < lowest_score:
        lowest_score = chi_scores[index]
        lowest_score_index = index               

# prints the decrypted message
print("The plaintext message is:", decrypted_messages[lowest_score_index])