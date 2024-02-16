import re

with open("aoc1.txt") as f: #f is a ref to the file 
    lines = f.readlines()   
    print(lines)

    added_numbers = 0

    for line in lines: #unpacks the list. access them one by one
        print(line) #dssmtmrkonedbbhdhjbf9hq

        x = re.findall("[0-9]", line)
        print(x) #'9'

        numbers = int(x[0] + x[-1]) #iterate through the lists and print first (x[0]) and last (x[-1]) numbers per line of list and add them up + (concatinates)
        print(numbers) #99
        added_numbers = numbers + added_numbers       

print(f"The sum of all of the calibration values is: {added_numbers}") #sum = 53921


