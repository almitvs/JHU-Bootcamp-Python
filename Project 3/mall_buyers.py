#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:23:28 2024

@author: Aidan Alme
@JHED aalme2
"""

import frac
import random

class Node:
    
    """Class for representing nodes"""
    
    def __init__(self, ID, connected_nodes, minimum_price, fractional_price, 
                 revenue = frac.Frac(0, 1)):
        """
        Method to initialize a fraction

        Parameters
        ----------
        ID : str
            the ID of the node.
        connected_nodes : list
            a list of connect node IDs.
        minimum_price : Frac
            the minimum price at the node.
        fractional_price : Frac
            the fractional price at the node.
        revenue : Frac, optional
            The revenue at the node. The default is frac.Frac(0, 1).

        Returns
        -------
        None.

        """
        self.ID = ID
        self.connected_nodes = connected_nodes
        self.minimum_price = minimum_price
        self.fractional_price = fractional_price
        self.revenue = revenue
        return
    
    # Overridden methods so nodes can be used in sets and dictionaries
    def __eq__(self, other):
        """
        A method to define equality between nodes

        Parameters
        ----------
        other : Node
            another node.

        Returns
        -------
        Bool
            True or false.

        """
        return self.ID == other.ID
        
    def __hash__(self):
        """
        A method to hash nodes

        Returns
        -------
        int
            the hash code for the node.

        """
        return hash(self.ID)
        
class Buyer:
    
    """Class for representing buyers"""
    
    def __init__(self, current_node_id, remaining_budget):
        """
        A method to initialize a buyer

        Parameters
        ----------
        current_node_id : str
            the ID of the node at which the buyer is currently.
        remaining_budget : Frac
            the remainibng budget of the buyer.

        Returns
        -------
        None.

        """
        self.current_node_id = current_node_id
        self.remaining_budget = remaining_budget
        return
        
def run_simulation(connectivities_file, pricing_file, budgets_file):
    """
    A method to run a simulation of buyers traversing the nodes

    Parameters
    ----------
    connectivities_file : str
        the file name which stores connections between nodes.
    pricing_file : str
        the file name which stores the prices at different nodes.
    budgets_file : str
        the file name which stores the budgets of the buyers.

    Returns
    -------
    total_revenue : Frac
        the total revenue earned among the malls.
    node_revenues : dictionary
        a dictionary of node IDs and their fraction of the revenue earned.

    """
    
    # Create a dictionary to store the nodes with their IDs as keys
    nodes = {}
    # Open the pricing file
    my_sample_file = open(pricing_file, 'r', encoding='utf-8-sig')
    # Iterate over the lines in the file
    for line in my_sample_file:
        # Split the line into entries
        split_line = line.rsplit()
        # Create a node based on the information in that line and store it
        # in the list of nodes
        nodes[split_line[0]] = Node(split_line[0], [], 
                               frac.Frac(split_line[1], split_line[2]), 
                               frac.Frac(split_line[3], split_line[4]))
    # Close the file
    my_sample_file.close()
    
    # Open the connectivities file
    my_sample_file = open(connectivities_file, 'r', encoding='utf-8-sig')
    # Iterate over the lines in the file
    for line in my_sample_file:
        # Split the line into entries
        split_line = line.rsplit()
        # Add the connectivity to the list of connectivites of the proper
        # node which is stored in the list of nodes
        nodes[split_line[0]].connected_nodes.append(split_line[1])     
    # Close the file
    my_sample_file.close()
    
    # Create a list to store the buyers
    buyers = []
    # Open the budgets file
    my_sample_file = open(budgets_file, 'r', encoding='utf-8-sig')
    # Iterate over the lines in the file
    for line in my_sample_file:
        # Split the line into entries
        split_line = line.rsplit()
        # Iterate through the entrys
        for budget in split_line:
            # Create a buyer with its budget that entry and store it
            # in the list of buyers; the buyer has a random starting node
            buyers.append(Buyer(random.choice(list(nodes.keys())), 
                          frac.Frac(budget, 1)))
    # Close the file
    my_sample_file.close()
    
    # Initialize the total revenue earned among the nodes
    total_revenue = frac.Frac(0, 1)
    # Iterate through the buyers to simulate their purchasing
    for buyer in buyers:
        # While the buyer can make a purchase in their current node
        while (buyer.remaining_budget >
               nodes[buyer.current_node_id].minimum_price):
            # The buyer spends the fractional price of their remaining budget
            spent = (buyer.remaining_budget * nodes[buyer.current_node_id].
                     fractional_price)
            # Update the buyer's remaining budget
            buyer.remaining_budget -= spent
            # Update the revenue of that node
            nodes[buyer.current_node_id].revenue += spent
            # Update the total revenue
            total_revenue += spent
            # If the buyer has a node to go to, update their current node
            if nodes[buyer.current_node_id].connected_nodes:
                buyer.current_node_id = random.choice(
                nodes[buyer.current_node_id].connected_nodes)
            # Otherwise break because they have nowhere else to go
            else:
                break
    
    # Initialize a dictionary for the nodes IDs and the fraction of the total
    # revenue which they earned
    node_revenues = {}
    # Iterate through the nodes
    for node in nodes.values():
        # Calculate the proportion of the revenue that node earned 
        node_revenues[node.ID] = node.revenue / total_revenue
    # Return the total revenue and the dictionary of nodes and revenues
    return total_revenue, node_revenues
    