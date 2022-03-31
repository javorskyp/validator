from parser import *
from scanner import *
import argparse

def cleaner(input_string, fix):
    if fix is True: print({input_string})
    line_full = False
    jump = False
    result = ''
    for symbol in input_string:
        if symbol == '#': jump = True
        elif jump is False and not symbol.isspace():
            if line_full is False: line_full = True
            result += symbol
        elif symbol == '\n':
            if line_full is True or (line_full is False and jump is False): result+= symbol
            line_full = False
            jump = False
    if fix is True: print(f'Instruction from cleaner for scanner \n--\n--\n{result}\n--\n--\n')
    return result

parser = argparse.ArgumentParser()
parser.add_argument('--clean', '-c', action='store_true', default=False )
parser.add_argument('--input', '-i', required=True )
args = parser.parse_args()

input_file = args.input
fix = args.clean

with open(input_file) as reader:
  input_string = reader.read()

input_string = cleaner(input_string, fix)
scanner = Scanner(input_string, fix)
parser = Parser(scanner, fix)
parser.start()