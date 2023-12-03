#!/usr/bin/env python
numberSpelling = {
    "0": 'zero',
    "1": 'one',
    "2": 'two',
    "3": 'three',
    "4": 'four',
    "5": 'five',
    "6": 'six',
    "7": 'seven',
    "8": 'eight',
    "9": 'nine'
}

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def find_number(a_str, number):
    numberIndexes = list(find_all(a_str, number))
    #comment this line to get solution to part 1
    letterIndexes = [] #list(find_all(a_str, numberSpelling[number]))
    all = numberIndexes + letterIndexes
    all.sort()
    return all

def find_all_numbers(a_str):
    numberIndexes = {
        "0": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": []
    }
    
    for number in numberSpelling:
        numberIndexes[number] = find_number(a_str, number)
    
    return numberIndexes

inputFile = '/home/dmontesinos/Sources/advent-of-code-2023/day1/input.txt'
total = 0

with open(inputFile, 'r') as f:
    for line in f:
        firstNumber = -1
        lastNumber = -1
        appearances = find_all_numbers(line)
        firstIndex = 9999999
        lastIndex = -1
        for number in appearances:
            if appearances[number]:
                if max(appearances[number]) > lastIndex:
                    lastIndex = max(appearances[number])
                    lastNumber = int(number)
                if min(appearances[number]) < firstIndex:
                    firstIndex = min(appearances[number])
                    firstNumber = int(number)

        total += firstNumber*10 + lastNumber
    
print(total)
