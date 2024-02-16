import regex as re

def convert(x:str): #variable defined to convert one to 1
    if x == "one" or x == "1":
        x = 1
    elif x == "two" or x == "2":
        x = 2
    elif x == "three" or x == "3":
        x = 3
    elif x == "four" or x == "4":
        x = 4
    elif x == "five" or x == "5":
        x = 5
    elif x == "six" or x == "6":
        x = 6
    elif x == "seven" or x == "7":
        x = 7
    elif x == "eight" or x == "8":
        x = 8
    elif x == "nine" or x == "9":
        x = 9
    return x

with open("aoc1.txt") as f: #f is a ref to the file 
    lines = f.readlines()   # read all lines of f (aoc1.txt)
    #print(lines)

    added_numbers = 0 #adds up the numbers of each line

    for line in lines: #unpacks the list. access them one by one
        print(line.strip()) #removes white space  dssmtmrkonedbbhdhjbf9hq
        number_list = []
        
        all_numbers = re.findall("\d|one|two|three|four|five|six|seven|eight|nine|zero", line, overlapped=True) # finds all the numbers (\d finds digits)
        #print(all_numbers)   #prints a list per line ['one', '9']
        
        for number in all_numbers: #iterates through all numbers
            x = convert(number) #calls convert function
            #print(x) #prints numbers as indiv str - need just the first and last
            number_list.append(x) #add converted numbers to a list 
                #convert each line back into a list and concatenate
        
        numbers = (str(number_list[0]) + str(number_list[-1]))
        print(numbers)

        added_numbers = int(numbers) + int(added_numbers)       
        
print(f"The sum of all of the calibration values is: {added_numbers}") #answer = 54676