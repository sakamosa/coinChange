""" CS 325 Project 2: Coin Change Group 13: Janel Buckingham,
Alisha-Crawley Davis, Sara Sakamoto """

import sys
import coinChange


#Get file name from commandline args
#inputFile = sys.argv[1]

#use for testing, skip the commandline
inputFile = 'test.txt'
outputFile = inputFile.replace(".txt", "change.txt")

#File contains:
# values[] = array of coin values on first line
# amount = int change to be made

# open files for reading/writing
in_file = open(inputFile, 'r')
out_file = open((outputFile), 'w')
#infinite looping ...
out_file.write(inputFile + "\n")
while (1):        
        # read a line from file
        values = in_file.readline()
        # if EOF or if line doesn't contain an array (second condition necessary on MSS_Problems.txt), break
        if (not values) or (len(values) < 2):
            break
        amount = in_file.readline()
        if (not amount):
                print "Error in file format: Amount needed\n"
                break


        # line is assigned an array created from the integers in line, removing brackets, whitespace, and delimiting commas
        values = [int(i) for i in values.replace("[","").replace(" ","").replace("]","").split(",")]
        #remove newline from amount, may not be necessary with latest file
        amount = int(amount.rstrip())

        results = coinChange.slowChange(values, amount)
        # write result as string to file
        out_file.write('[')
        coins = results[0]
        for c in coins[:-1]:
                out_file.write(str(c) + ', ')
        for last in coins[-1:]:
                out_file.write(str(last) + ']')
        out_file.write('\n')
        out_file.write(str(results[1]))
        out_file.write('\n\n')

# rewind to beginning of file and do it again with algorithm 2...
out_file.write(inputFile + "\n")
in_file.seek(0)
while (1):
        # read a line from file
        values = in_file.readline()
        # if EOF or if line doesn't contain an array (second condition necessary on MSS_Problems.txt), break
        if (not values) or (len(values) < 2):
                break
        amount = in_file.readline()
        if (not amount):
                print "Invalid file format, must contain amount of change to be made\n"
                break
        # line is assigned an array created from the integers in line, removing brackets, whitespace, and delimiting commas
        values = [int(i) for i in values.replace("[","").replace(" ","").replace("]","").split(",")]
        amount = int(amount.rstrip())
        results = coinChange.greedy(values, amount)
        # write result as string to file
        out_file.write('[')
        coins = results[0]
        for c in coins[:-1]:
                out_file.write(str(c) + ', ')
        for last in coins[-1:]:
                out_file.write(str(last) + ']')
        out_file.write('\n')
        out_file.write(str(results[1]))
        out_file.write('\n\n')

# rewind to beginning of file and do it again with algorithm 3...
out_file.write(inputFile + "\n")
in_file.seek(0)
while (1):
        # read a line from file
        values = in_file.readline()
        # if EOF or if line doesn't contain an array (second condition necessary on MSS_Problems.txt), break
        if (not values) or (len(values) < 2):
                break
        amount = in_file.readline()
        if (not amount):
                print "Invalid file format, must contain amount of change to be made\n"
                break
        # line is assigned an array created from the integers in line, removing brackets, whitespace, and delimiting commas
        values = [int(i) for i in values.replace("[","").replace(" ","").replace("]","").split(",")]
        amount = int(amount.rstrip())
        results = coinChange.dynamic(values, amount)
        # write result as string to file
        out_file.write('[')
        coins = results[0]
        for c in coins[:-1]:
                out_file.write(str(c) + ', ')
        for last in coins[-1:]:
                out_file.write(str(last) + ']')
        out_file.write('\n')
        out_file.write(str(results[1]))
        out_file.write('\n')

# close files
out_file.close()
in_file.close()


