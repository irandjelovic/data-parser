#!/usr/bin/env python
'''
Simple string parser module with function(s):
    - Remove adjacent pairs of same letters for an input string
'''


# standard lib
import argparse


arg_parser = argparse.ArgumentParser(description="Argument parser")
arg_parser.add_argument('-i', dest="input", help="Input string")
arg_parser.add_argument('-r', action="store_true", dest="recursion", help="Call recursion function")


def remove_adjacent_same_letters(input_str):
    # return if input length is less than two letters
    if not input_str or len(input_str) < 2:
        return input_str
    
    i = 0
    while i < len(input_str) - 1:
        if input_str[i] == input_str[i+1]:
            # if same letters, then cut them
            input_str = input_str[:i] + input_str[i+2:]
            if i > 0:
                # if same letters, move index pointer to previous letter
                i -= 1
        else:
            # if letters are not the same continue with processing
            i += 1

    return input_str


def remove_adjacent_same_letters_recursion(input_str):
    # return if input length is less than two letters
    if not input_str or len(input_str) < 2:
        return input_str
    
    found_same_letters = False
    parsed_input = ''
    
    i = 0
    while i < len(input_str):
        # append letter if it's the last letter or adjacent letters are not the same
        if i == len(input_str) - 1 or input_str[i] != input_str[i+1]:
            parsed_input += input_str[i]
            i += 1
        else:
            found_same_letters = True
            i += 2
    
    if found_same_letters:
        return remove_adjacent_same_letters_recursion(parsed_input)
    
    return parsed_input


def main():
    args = arg_parser.parse_args()
    
    if args.recursion:
        func = remove_adjacent_same_letters_recursion
    else:
        func = remove_adjacent_same_letters
    
    print "Input: {}".format(args.input)
    output = func(args.input)
    print "Output: {}".format(output)


if __name__ == "__main__":
    main()
