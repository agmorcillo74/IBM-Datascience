# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:59:30 2020

@author: Toni
"""



import csv
board = 'csv/boardgames.csv'

with open(board) as b:
    b = csv.reader(b)
    header_row = next(b)
    print(header_row)