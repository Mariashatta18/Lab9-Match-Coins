"""
Program: Match Coins Game - Coin Class
Author: Mariam Shatta
Purpose: This file defines the Coin class used in the Match Coins game.
         The coin can be tossed and can return whether it landed on Heads or Tails.
Starter Code: No starter code used.
Date: September 28, 2026
"""

import random


class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup
