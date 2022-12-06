import os 
import string
from functools import reduce
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = "input_day4.txt"

x = [l.strip() for  l in open(filename)]