#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:23:54 2024

@author: Aidan Alme
@JHED aalme2
"""

class Frac:
    
    """Class for representing and operating on fractions"""
    
    def __init__(self, num, den):
        """
        Initializes the fraction

        Parameters
        ----------
        num : int
            numerator.
        den : int
            denominator.

        Returns
        -------
        None.

        """
        self.num = int(num)
        self.den = int(den)
    
    def simplify(self):
        """
        Method for simplifying a fraction

        Returns
        -------
        Frac
            the simplified fraction.

        """
        # Stores the numerator and denominator to use in calculations
        num = self.num
        den = self.den
        # If the numerator is zero, return a fraction object 0/1
        if num == 0:
            return Frac(0, 1)
        # If the numerator is bigger than the denominator find the GCF
        elif (num > den):
            # Find the GCF
            rem = num % den
            # If the GCF is zero, deivide by the denominator
            if rem == 0:
                return Frac(num / den, den / den)
            # Divide by the GCF
            elif rem != 1 and num % rem == 0 and den % rem == 0:
                return Frac(num / rem, den / rem)
            # Otherwise the fraction is already simplified
            else:
                return Frac(num, den)
        # If the numerator is less than the denominator find the GCF
        elif (num < den):
            # Find the GCF
            rem = den % num
            # If the GCF is zero, deivide by the numerator
            if rem == 0:
                return Frac(num / num, den / num)
            # Divide by the GCF
            elif rem != 1 and num % rem == 0 and den % rem == 0:
                return Frac(num / rem, den / rem)
            # Otherwise the fraction is already simplified
            else:
                return Frac(num, den)
        # If the numerator and denominator are equal, return 1/1
        else:
            return Frac(1, 1)
    
    def __add__ (self, other):
        """
        A method to add fractions

        Parameters
        ----------
        other : Frac
            The fraction to be added.

        Returns
        -------
        Frac
            the sum.

        """
        # Finds the common denominator, adds, and simplifies
        return Frac(self.num * other.den + other.num * self.den, self.den * 
               other.den).simplify()
    
    def __sub__ (self, other):
        """
        A method to subtract fractions

        Parameters
        ----------
        other : Frac
            The fraction to be subtracted.

        Returns
        -------
        Frac
            the difference.

        """
        # Finds the common denominator, subtracts, and simplifies
        return Frac(self.num * other.den - other.num * self.den, self.den * 
               other.den).simplify()
        
    def __mul__ (self, other):
        """
        A method to multiply fractions

        Parameters
        ----------
        other : Frac
            The fraction to be multiplied.

        Returns
        -------
        Frac
            The product.

        """
        # Finds the common denominator, multiplies, and simplifies
        return Frac(self.num * other.num, self.den * other.den).simplify()
        
    def __truediv__ (self, other):
        """
        A method to divide fractions

        Parameters
        ----------
        other : Frac
            The fraction to divide.

        Returns
        -------
        Frac
            The quotient.

        """
        # Finds the common denominator, divides, and simplifies
        return Frac(self.num * other.den, self.den * other.num).simplify()
    
    def __str__(self):
        """
        A method to represent a fraction as a string

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.num) + "/" + str(self.den)
    
    def __gt__(self, other):
        """
        A method to compare if a fraction is greater than another

        Parameters
        ----------
        other : Frac
            A fraction to compare to.

        Returns
        -------
        Bool
            Whether the statement is true or false.

        """
        return self.num / self.den > other.num / other.den

        
        