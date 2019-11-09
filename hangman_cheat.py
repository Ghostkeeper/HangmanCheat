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

