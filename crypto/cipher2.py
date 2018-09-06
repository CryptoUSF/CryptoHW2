"""
Andrew Egly
Homework 2 Cryptanalysis

This program outputs the frequency of characters in a file,
as well as testing the I.C. (Index of Coincidence) to see how close
to a real English sentence the string possibly is.
"""

import collections


"""make copy txt file into all caps and removing all non-letters, used in HW1"""
def fileFormat(txtFile):
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ch = []
    # open the file to read
    openText = open(txtFile, 'r')
    # base case for non-numbers
    for l in openText:
        for c in l:
            # add letters into the list
            if c in key:
                ch.append(c.upper())
            # remove spaces and non-letters
            else:
                pass
            # make list of characters into a single string
    chString = ''.join(ch)
    openText.close()
    return chString


"""this checks frequency of letters or groups of letters in a file. Calls findIC"""
def polyBreak(size, eString):
    size = int(size)
    # initialize a dictionary
    dict = {}

    # run frequency algorithm on string
    for l in range(len(eString) - size - 1):
        narr = eString[l:l+size]
        if narr in dict:
            dict[narr] += 1
        else:
            dict[narr] = 1

    # print frequency list
    print("\n".join("{}: {}".format(k, v) for k, v in dict.items()))

    # calc the I.C. of the cipher
    print("\n")
    findIC(eString, dict)
    # return the frequency list
    return dict


"""Used to find the I.C. of the sequences of characters in a file. Uses collections import."""
def findIC(eString, dict):
    print("Index of Coincidence:")
    N = len(eString)
    freqs = collections.Counter(dict)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    freqsum = 0.0

    # calculating the I.C. of the cipher
    counter=0
    sLength = len(next(iter(dict)))
    while counter < sLength:
        for l in alphabet:
            # combine the characters that are alike
            freqsum += freqs[l] * (freqs[l] - 1)
        # divide by the size of the file
        IC = freqsum / (N*(N-1))
        counter += 1
        # print out the seqences. The lower the decimal, the closer to a possible sentence the file is
        print("sequence "+ str(counter) +": %.3f" % IC, "({})".format(IC))

    return IC


"""Main class used to run all the functions. Calls fileformat and polyBreak."""
class main():
    # read in file
    eString = fileFormat(input("Please paste the path to the file being tested: "))
    eString = eString.upper()

    # get the size of the gram (monogram, bigram, trigram, etc)
    answer = input("Please input the \"n\" amount for gram (1=mono,2=bi, 3=tri): ")

    finalDict = polyBreak(answer, eString)

