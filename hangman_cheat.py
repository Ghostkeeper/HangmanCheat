#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2019 Ghostkeeper
# This package is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This package is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
# You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

"""
This program allows cheating in a hangman game. It will select the optimal
letter for you to guess.

Usage: At every step, type in the word with asterisks where the letter is still
unknown. For example:
>>> *******    # We start with a 7-letter word.
<<< 'e'        # The program guesses the letter E.
>>> *******    # This was not in the word, so you still need to type 7 characters.
<<< 'a'        # The program guesses the letter A.
>>> *a***a*    # This was in the word twice.
<<< 'n'        # The program guesses the letter N.
>>> *an**an    # This was also in the word twice.
<<< 'm'        # The program guesses the letter M.
>>> *an*man    # This was in the word as well in the 5th location.
<<< 'h'        # Very few options remain. The program guesses the letter H.
>>> han*man    # Yup, good guess.
<<< 'g'        # The program guesses a G as the final letter.
>>> hangman    # The word is complete.
               # The program terminates as there are no more letters to guess.
"""


import functools
import re

with open("dictionary.txt") as f:
	word_list = [word.strip() for word in f.readlines()]

all_symbols = set()
for word in word_list:
	for symbol in word:
		all_symbols.add(symbol)

def filter_candidates(query, remaining_symbols):
	remaining_symbols_re = "[" + re.escape("".join(remaining_symbols)) + "]"
	query_re = "^" + re.escape(query).replace("\\*", remaining_symbols_re) + "$"
	compiled = re.compile(query_re)
	yield from filter(functools.partial(re.match, compiled), word_list)

def guess_safest(query, remaining_symbols):
	"""
	Guesses the letter that has the least chance of not being present in the
	word.
	:param query: The remaining query, with asterisks in place of unknowns.
	:param remaining_symbols: The characters to guess from.
	:return: The character to guess.
	"""
	commonality = {symbol: 0 for symbol in remaining_symbols}  # Initialise to 0.
	candidates = filter_candidates(query, remaining_symbols)
	for candidate in candidates:
		for symbol in remaining_symbols:
			if symbol in candidate:
				commonality[symbol] += 1

	return max(remaining_symbols, key=lambda symbol: commonality[symbol])  # Return most common symbol.

if __name__ == "__main__":
	remaining_symbols = all_symbols.copy()
	print("Let me guess the word!")
	query = input("")
	while "*" in query:
		for symbol in query:
			if symbol != "*" and symbol in remaining_symbols:
				remaining_symbols.remove(symbol)
		guess = guess_safest(query, remaining_symbols)
		print(guess)
		remaining_symbols.remove(guess)
		query = input("")