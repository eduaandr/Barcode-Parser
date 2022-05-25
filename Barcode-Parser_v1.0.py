# Bardcode-Parser
# Description: Program that parses the barcode digits from invoice registries
# Author: Eduardo Andrade
# Date: 2022/04/30
# Version: 1.0

# import csv library
import csv
    
# initiate the integer for total raw registries counter
count_current = 0

# initiate the integer for parsed registries counter. Ideally count_current = count_parsed
count_parsed = 0

# initiate the integer for exception registries counter
count_exception = 0

# initiate the array for raw registries
string_raw = []

# initiate the array for parsed registries
string_parsed = []

# open the specified .csv file. Replace string >>filelocation<< with the actual file's directory
with open(r">>filelocation<<\Sample_Raw.csv") as file:

    # assign the opened file to variable reader
    reader = csv.reader(file)

    # loop that scans all the registries within variable reader
    for row in reader:

        # append scanned row to string_raw
        string_raw.append(str(row))

        # assign string_raw to string_aux 
        string_aux = string_raw[count_current]

        # try to search for a character sequence
        try:

            # look for 3522 sequence in the row
            index = string_aux.index('3522')

            # append the invoice 44-digit number of the scanned row to string_parsed
            string_parsed.append(string_aux[index:(index + 44)])

            # increment count_parsed
            count_parsed = count_parsed + 1

        # if it does not find it, it will probably return the ValueError exception
        except ValueError:

            # increment count_exception
            count_exception = count_exception + 1

        # increment count_current
        count_current = count_current + 1

# get the total counted rows
count_total = count_current

# create the specified .txt file. Replace string >>filelocation<< with the actual file's directory
file = open(r">>filelocation<<\Sample_Parsed.txt", "w+")

# initiate the integer i
i = 0

# scans all registries in count_parsed
while i < count_parsed:

    # write the corresponding index to file
    file.write(string_parsed[i])

    # inset line break in file
    file.write("\n")

    # increment i
    i = i + 1

# print total counter
print("Total:", count_total)

# print parsed counter
print("Parsed:", count_parsed)

# print exceptions counter
print("Exceptions:", count_exception)
