""" CS 325 Project 2: Coin Change Group 13: Janel Buckingham,
Alisha-Crawley Davis, Sara Sakamoto """

import sys
import coinChange
import time
import timeit
from timeit import Timer

#Open file to store timing information
myFile = "timingInfo.txt"
target = open(myFile, 'w')

#Get file name from commandline args
if len(sys.argv) != 2:
    print("Correct usage: python main.py nameOfFile.txt")
    sys.exit()

inputFile = sys.argv[1]

#use for testing, skip the commandline
outputFile = inputFile.replace(".txt", "change.txt")

#File contains:
# values[] = array of coin values on first line
# amount = int change to be made

# open files for reading/writing
in_file = open(inputFile, 'r')
out_file = open((outputFile), 'w')
#infinite looping ...
out_file.write(inputFile + " - slowchange, not run if n > 18\n")
target.write("slow, ")
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
        if amount < 19:       
            startTime = timeit.default_timer()
            results = coinChange.slowChange(values, amount)
            target.write(str(timeit.default_timer() - startTime))
            target.write(", ")
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
        else:
            target.write("X, ")
target.write("\n")

# rewind to beginning of file and do it again with algorithm 2...
out_file.write(inputFile + " - greedy\n")
in_file.seek(0)
target.write("greedy, ")
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
        startTime = timeit.default_timer()
        results = coinChange.greedy(values, amount)
        target.write(str(timeit.default_timer() - startTime))
        target.write(", ")
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
target.write("\n")
# rewind to beginning of file and do it again with algorithm 3...
out_file.write(inputFile + " - DP\n")
in_file.seek(0)
target.write("dp, ")
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
        startTime = timeit.default_timer()
        results = coinChange.dynamic(values, amount)
        target.write(str(timeit.default_timer() - startTime))
        target.write(", ")
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
target.write("\n")
# close files
out_file.close()
in_file.close()
target.close()

