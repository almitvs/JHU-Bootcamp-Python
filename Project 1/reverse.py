#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:47:10 2024

@author: Aidan Alme
@JHED: aalme2
"""

# Prompt for user input
encrypted_message = input("Enter the encrypted message: ")

# Create an empy string for the plaintext message
decrypted_message = ""

# Iterate throught the characters in the message to decrypt them
for char in encrypted_message:
    # Decode the standard lowercase alphabetic characters
    if ord(char) >= 97 and ord(char) <= 122:
        # Uses ASCII values in a decryption algorithm
        decrypted_message += (chr(-1 * ord(char) + 219))
    # Leave all other characters as is    
    else:
        decrypted_message += char    

# Print the decrypted message    
print("The plaintext message is:", decrypted_message)