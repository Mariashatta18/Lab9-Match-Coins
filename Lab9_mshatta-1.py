"""
Program: Match Coins Game
Author: Mariam Shatta
Purpose: This program runs a coin matching game between two players.
         Each player starts with 20 coins. If the coins match, Player 1
         wins a coin. If they do not match, Player 2 wins a coin.
Starter Code: No starter code used.
Date: September 28, 2026
"""

from player import Player


def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    play = input("\nDo you want to toss the coins? (y/n): ")

    while play.lower() == "y":
        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a Match! Player 1 wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("...No Match! Player 2 wins a coin.")

        print(f"\n{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        play = input("\nDo you want to toss the coins? (y/n): ")

    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 wins the game!")
    else:
        print("It's a draw!")


main()
