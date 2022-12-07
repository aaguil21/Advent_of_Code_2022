import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = "input_day7.txt"

x = [l.strip() for  l in open(filename)]