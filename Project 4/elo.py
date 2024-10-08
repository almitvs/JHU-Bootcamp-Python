#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:07:39 2024

@author: Aidan Alme
@JHED: aalme2
"""

import math
import matplotlib.pyplot as plt
import pandas as pd
import random
import seaborn as sns

def calculate_win_probability (rating_a, rating_b):
    """
    Method to calculate the probability of player A winning; the probability
    of Player B is 1 minus that of PLayer A

    Parameters
    ----------
    rating_a : float
        The Elo rating of a given player.
    rating_b : float
        The Elo rating of another player.

    Returns
    -------
    float
        The probability of player A winning.

    """
    # Calculate the probability according to Elo's scheme
    return (math.exp((rating_a - rating_b) / 100) / 
           (1 + math.exp((rating_a - rating_b) / 100)))

def calculate_ratings (past_matches_file):
    """
    Method to calculate the ratings for a group of players based on
    Past match outcomes

    Parameters
    ----------
    past_matches_file : string
        The name of a csv file containing the results of past matches.

    Returns
    -------
    ratings : dict
        A dictionary in which the keys are player names and the values their
        respective ratings.

    """
    try:
        # Read the csv file
        past_matches = pd.read_csv(past_matches_file, index_col = 0)
    except:
        # Throw an error if an incorrect file name is given
        print("File not found")
    else:
        # If the file works, create a dictionary
        ratings = {num : 1500.0 for num in range(8)}
        
        # Iterate through the rows
        for index, row in past_matches.iterrows():
            # Use the winner as A and the loser as B 
            # in the calculate_win_probability formula
            player_a = int(row['winner'])
            player_b = int(row['loser'])
            
            prob_winner = calculate_win_probability(ratings[player_a],
                                                    ratings[player_b])
            
            # Adjust the ratings based on win probability
            ratings[player_a] += 5 * (1.0 - prob_winner)
            ratings[player_b] += 5 * (0.0 - (1 - prob_winner))
        # Return the ratings
        
        return ratings

def check_valid_dictionary (ratings):
    """
    Method to check if a given dictionary contains 8 players with the names 0-7
    and values with their ratings or probabilities

    Parameters
    ----------
    ratings : dict
        A dictionary.

    Returns
    -------
    None.

    """
    # Throw an error if there are more than 8 players
    assert len(ratings) == 8, "Dictionary has incorrect number of entries"
    # Throw an error if the players have the wrong names
    for index, player in enumerate(list(ratings.keys())):
        assert index == player, "Incorrect player name"
    # Throw an error if the values are not floats
    for index, rating in enumerate(list(ratings.values())):
        if (isinstance(rating, float) == False and 
            isinstance(rating, int) == False):
            raise Exception("Ratings are not numbers")
    return
            
def display_ratings (ratings):
    """
    A method to display the ratings of a given dictionary of players

    Parameters
    ----------
    ratings : dict
        A dictionary of 8 players and their ratings.

    Returns
    -------
    None.

    """
    # Check if the input meets the specifications
    check_valid_dictionary (ratings)
    # Print the ratings to the terminal
    print(ratings)
    
    # Create and save a bar graph of the players and their ratings
    sns.set_context("poster")
    chart = sns.barplot(x = list(ratings.keys()), y = list(ratings.values()))
    chart.set_xlabel("Players")
    chart.set_ylabel("Rating")
    plt.tight_layout()
    plt.savefig('projections.pdf')
    plt.show()
    return

def find_winner (ratings, player_a, player_b):
    """
    A method to determine the winner of a match between two players

    Parameters
    ----------
    ratings : dict
        A valid dicitonary of players and their ratings.
    player_a : string
        The name of a player.
    player_b : string
        The name of another player.

    Returns
    -------
    String
        The name / key of the winning player.

    """
    # Calculate the probability of A winning based on ELo's formula
    delta = (float(ratings[player_a]) - float(ratings[player_b])) / 100
    prob_a = math.exp(delta) / (1 + math.exp(delta))
    
    # Generate a random number and randomly determine the winner based on
    # the prboability of A winning
    num = random.uniform(0, 1)
    if num < prob_a:
        return player_a
    else:
        return player_b
    
def project_win_probs (ratings):
    """
    A method to project the probability of players winning based on their Elos
    and several simulations

    Parameters
    ----------
    ratings : dict
        A valid dictionary of players and their ratings.

    Returns
    -------
    win_probs : dict
        A dictionary of players and their probabilities of winning.

    """
    # Check that the input is valid
    check_valid_dictionary (ratings)
    
    # Create a empty dictionary for the players and their probabilities
    win_probs = {num : 0.0 for num in range(8)}
    
    # Simulate a single-elimination tournament with set matchups 100 times then
    # divide the number of wins by 100 to calculate the probability
    for num in range(100):
        winner = find_winner(ratings, find_winner(ratings, 
                                                  find_winner(ratings, 0, 7), 
                                                  find_winner(ratings, 1, 6)), 
                             find_winner(ratings, find_winner(ratings, 2, 5), 
                                         find_winner(ratings, 3, 4)))
        win_probs[winner] += 1
    for player in list(win_probs.keys()):
        win_probs[player] /= 100
    return win_probs

def display_probs (win_probs):
    """
    A method to display and download the probabilities of the players winning

    Parameters
    ----------
    ratings : dict
        A dictionary of players and their probabilities.

    Returns
    -------
    None.

    """
    # Check the dictionary is valid
    check_valid_dictionary (win_probs)
    
    # Create a list of tuples based on each player and their probability
    sorted_players = [(a, b) for a, b in win_probs.items()]
    # Sort tuples based on their ratings
    sorted_players.sort(key = lambda y : y[1], reverse = True)
    
    # Create and save a csv with the player names and their probabilities
    dfr = pd.DataFrame(sorted_players)
    dfr.to_csv('probs.csv')
    
    # Create and save a pie chart with the player names and their probabilities
    plt.pie(list(win_probs.values()), labels = list(win_probs.keys()))
    plt.savefig('projections_pie.pdf')
    plt.show
    return
    