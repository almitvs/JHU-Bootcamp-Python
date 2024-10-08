import random

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:03:24 2024

@author: Aidan Alme
@JHED aalme2
"""

def encode_sequence (user_input):
    """
    Function to encrypt a message with DNA
    
    Parameters
    ----------
    user_input : string
        the message to encrypt.

    Returns
    -------
    dna_code : string
        the encypted message.

    """
    #Initialize the encoded message
    dna_code = ""
    #Iterate through each character in the message
    for char in user_input:
        #The binary number of the character for this iteration
        binary_num = ""
        #The ASCII value of the character
        char_num = ord(char)
        #Create an 8 digit binary value for the ASCII value
        for num in range(7, -1, -1):
            binary_num += str(char_num // (2 ** num))
            char_num = (char_num % (2 ** num))
        #Replace every 2 values with DNA molecules    
        for num in range(0, len(binary_num), 2):
            if binary_num[num : num + 2] == '00':
                dna_code += 'A'
            elif binary_num[num : num + 2] == '01':
                dna_code += 'T'
            elif binary_num[num : num + 2] == '10':
                dna_code += 'C'
            elif binary_num[num : num + 2] == '11':
                dna_code += 'G'
    return dna_code

def decode_sequence (user_input):
    """
    Function to decode a DNA-coded message

    Parameters
    ----------
    user_input : string
        the encrypted message.

    Returns
    -------
    decoded_sequence : string
        the decrypted message.

    """
    #Initialize the decoded message
    decoded_sequence = ""
    #Iterate through every 4 letters as those combined are 1 number
    for num in range(0, len(user_input), 4):
        #Initialize the binary number for the given character
        binary_num = ""
        #Convert 4 characters into a binary number
        for char in user_input[num : num + 4]:
            if char == 'A':
                binary_num += '00'
            elif char == 'T':
                binary_num += '01'
            elif char == 'C':
                binary_num += '10'
            elif char == 'G':
                binary_num += '11'    
        char_num = 0
        #Convert the binary number to a decimal number then a character
        for index, char in enumerate(binary_num):
            char_num += (2 ** (7 - index)) * int(char)
        #Add the character to the decoded message    
        decoded_sequence += chr(char_num)   
    return decoded_sequence

def encrypt_decrypt (user_input, key = "CAT"):
    """
    Function to encrypt a DNA-encrypted message using the XOR method

    Parameters
    ----------
    user_input : string
        a DNA-encrypted message.
    key : string, optional
        a key of DNA molecules. The default is "CAT".

    Returns
    -------
    encryption : string
        a XOR-encrypted DNA encryption.

    """
    #Initialize the encryption with the user input
    encryption = user_input
    #Encrypt the message once for each character in the key
    for key_char in key:
        #A set to compare with the sequence key to determine encryption
        key_set = set([key_char])
        #The newly encrypted sequence
        new_encryption = ""
        #Encrypt each character in the sequence
        for char in encryption:
            #A set for the purpose of symmetric comparison
            char_set = set([char])
            if key_set | char_set == set(['A']):
                new_encryption += 'A'
            elif key_set | char_set == set(['A', 'T']):
                new_encryption += 'T'
            elif key_set | char_set == set(['A', 'C']):
                new_encryption += 'C'
            elif key_set | char_set == set(['A', 'G']):
                new_encryption += 'G'
            elif key_set | char_set == set(['T']):
                new_encryption += 'A'
            elif key_set | char_set == set(['T', 'C']):
                new_encryption += 'G'
            elif key_set | char_set == set(['T', 'G']):
                new_encryption += 'C'    
            elif key_set | char_set == set(['C']):    
                new_encryption += 'A'
            elif key_set | char_set == set(['C', 'G']):  
                new_encryption += 'T'
            elif key_set | char_set == set(['G']):  
                new_encryption += 'A'
        encryption = ""
        #Add the character to the new sequence
        encryption += new_encryption
    return encryption   
                
def synthesizer (sequence):
    """
    A function to model the fallible synthesization of DNA

    Parameters
    ----------
    sequence : string
        a DNA sequence to synthesize.

    Returns
    -------
    new_sequence : string
        the synthesized sequence.

    """
    #Initialize the new sequence
    new_sequence = ""
    #Synthesizes each character in the sequence
    for char in sequence:
        #Generates a random to use in the probabilities of error
        random_num = random.randrange(1, 101, 1)
        #Depending on the character and the random number, a given character
        #is synthesized. Ranges of numbers in the conditionals correspond to
        #error probabilities
        if char == 'A':
            new_sequence += 'A'
        elif char == 'T':
            if random_num >= 1 and random_num <= 5:
                new_sequence += 'A'
            elif random_num >= 6 and random_num <= 95:
                new_sequence += 'T'
            elif random_num >= 96 and random_num <= 98:
                new_sequence += 'C'
            else:
                new_sequence += 'G'
        elif char == 'C':
            if random_num == 1:
                new_sequence += 'A'
            elif random_num == 2:
                new_sequence += 'T'
            elif random_num >= 3 and random_num <= 99:
                new_sequence += 'C'
            else:
                new_sequence += 'G'
        elif char == 'G':
            if random_num == 1:
                new_sequence += 'A'
            elif random_num == 2 or random_num == 3:
                new_sequence += 'T'
            elif random_num == 4 or random_num == 5:
                new_sequence += 'C'
            else:
                new_sequence += 'G'
    return new_sequence

def error_count (string_1, string_2):  
    """
    A function to count the different characters between two strings

    Parameters
    ----------
    string_1 : string
        the correct string.
    string_2 : string
        the string with errors.

    Returns
    -------
    num_mismatches : int
        the number of errors.

    """
    #Initialize the number of errors
    num_mismatches = 0
    #Iterates through each character
    for index, char in enumerate(string_1):
        #Increments the error count
        if char != string_2[index]:
            num_mismatches += 1
    return num_mismatches

def redundancy (num, sequence):
    """
    Synthesizes multiple times and picks the likely molecule to reduce error

    Parameters
    ----------
    num : int
        the number of synthesis trials.
    sequence : string
        the DNA sequence to synthesize.

    Returns
    -------
    corrected_sequence : string
        the correct DNA-encrypted sequence.

    """
    #Initialize a list to store all the synthesized sequences
    sequences = []
    #Initialize the corrected sequence
    corrected_sequence = ""
    #Generate synthesized sequences
    for num in range(0, num, 1):
        sequences.append(synthesizer(sequence))
    #Correct each character one at a time    
    for num in range(0, len(sequence), 1):
        #A list to store character frequencies where index 1=A, 2=T, 3=C, 4=G
        frequencies = [0] * 4
        #Count the occurence of each letter in the place of the given index
        for entry in sequences:
            if entry[num] == 'A':
                frequencies[0] += 1
            elif entry[num] == 'T':
                frequencies[1] += 1
            elif entry[num] == 'C':
                frequencies[2] += 1
            elif entry[num] == 'G':
                frequencies[3] += 1
        #Find the index, thus DNA molecule, that occurs the most        
        maximum = frequencies.index(max(frequencies))
        #Add the molecule to the sequence
        if maximum == 0:
            corrected_sequence += 'A'
        elif maximum == 1:
            corrected_sequence += 'T'
        elif maximum == 2:
            corrected_sequence += 'C'
        elif maximum == 3:
            corrected_sequence += 'G'
    return corrected_sequence
        