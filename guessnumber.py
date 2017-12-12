#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:12:58 2017

@author: Dustin
"""
guess = 50
high = 100
low = 0
print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(guess) + "?")
answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while answer != "h" and answer != "l" and answer != "c":
    print("Sorry, I did not understand your input.")
    print("Is your secret number " + str(guess) + "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while answer == "h" or answer == "l":
    if answer == "h":
        high = guess
        guess = int((low + high)/2)
        print("Is your secret number " + str(guess) + "?")
        answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")       
        while answer != "h" and answer != "l" and answer != "c":
            print("Sorry, I did not understand your input.")
            print("Is your secret number " + str(guess) + "?")
            answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    else:
        low = guess
        guess = int((low + high)/2)
        print("Is your secret number " + str(guess) + "?")
        answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")        
        while answer != "h" and answer != "l" and answer != "c":
            print("Sorry, I did not understand your input.")
            print("Is your secret number " + str(guess) + "?")
            answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
print("Game over. Your secret number was: " + str(guess)) 