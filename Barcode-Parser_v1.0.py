# BardcodeParser
# Description: Program to parse invoice registries from csv files
# Date: 2022/04/30
# Version: 1.0

# import csv library
import csv

# open the specified .csv file
with open(r"C:\Users\eduaa\Documents\GAAR\NFs\InvoiceParser\Version_2.0\codes_202204171059522.csv") as file:

    # assign the opened file to variable reader
    reader = csv.reader(file)

    # initiate the integer for total raw registries counter
    count_current = 0

    # initiate the integer for parsed registries counter. Ideally count_Current = count_parsed
    count_parsed = 0

    # initiate the integer for exception registries counter
    count_exception = 0

    # initiate the array for raw registries
    string_raw = []

    # initiate the array for parsed registries
    string_parsed = []

    # loop that scans all the registries within variable reader
    for row in reader:

        # append scanned row to variable string_raw
        string_raw.append(str(row))

        # assign string_raw to string_aux variable
        string_aux = string_raw[count_current]

        # try to search for a character sequence
        try:

            # look for 3522 sequence in the row
            index = string_aux.index('3522')

            # append the invoice 44-digit number of the scanned row to variable string_parsed
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

    # create the specified .txt file
    file = open(r"C:\Users\eduaa\Documents\GAAR\NFs\InvoiceParser\Version_2.0\MyFile.txt", "w+")

    # initiate the integer i
    i = 0

    # scans all count_parsed variables
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
