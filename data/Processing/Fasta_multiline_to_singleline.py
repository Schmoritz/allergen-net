#!/usr/bin/env python
# coding: utf-8

# In[38]:


#!/usr/bin/env python 
# Created by: Lee Bergstrand 
# Descript: Converts multiline FASTAs to single line FASTAs
#  
# Usage: FastaMLtoSL.py <sequences.faa> 
# Example: FastaMLtoSL.py mySeqs.faa
#
# Altered by: Alexander Kaier
# Descript: Deleting sequence headers and appending ";1" to each sequence as allergen header
# Date: 15.05.2019
#
#----------------------------------------------------------------------------------------
#===========================================================================================================
#Imports:
	
import sys, re, string
#===========================================================================================================
# Functions:

# 1: Checks if in proper number of arguments are passed gives instructions on proper use.
def argsCheck(numArgs):
    if len(sys.argv) < numArgs or len(sys.argv) > numArgs:
        print("Converts multiline FASTAs to single line FASTAs")
        print("By Lee Bergstrand\n")
        print("Usage: " + sys.argv[0] + " <sequences.fasta>")
        print("Examples: " + sys.argv[0] + " mySeqs.fasta")
        exit(1) # Aborts program. (exit(1) indicates that an error occurred)
#===========================================================================================================
# Main program code:

# House keeping...
argsCheck(2) # Checks if the number of arguments are correct.

# Stores file one for input checking.
inFile  = sys.argv[1]
outFile = inFile.replace(".fasta", "_one_liner.txt")

print(">> Opening FASTA file...")
# Reads sequence file list and stores it as a string object. Safely closes file:
try:
    with open(inFile,"r") as newFile:
        sequences = newFile.read()
        sequences = re.split("^>", sequences, flags=re.MULTILINE) # Only splits string at the start of a line.
        del sequences[0] # The first fasta in the file is split into an empty empty element and and the first fasta
                         # Del removes this empty element.
        newFile.close()
except IOError:
    print("Failed to open " + inFile)
    exit(1)

print(">> Converting FASTA file from multiline to single line and writing to file.")
# Conversts multiline fasta to single line. Writes new fasta to file.
try:
    with open(outFile,"w") as newFasta:
        for fasta in sequences:
            try:
                header, sequence = fasta.split("\n", 1) # Split each fasta into header and sequence.
            except ValueError:
                print(fasta)
            header = ">" + header + "\n" # Replace ">" lost in ">" split, Replace "\n" lost in split directly above.
            sequence = sequence.replace("\n","") + ";1\n" # Replace newlines in sequence, remember to add one to the end.
            newFasta.write(sequence)
        newFasta.close()
except IOError:
    print("Failed to open " + inFile)
    exit(1)

print(">> Done!")
#===========================================================================================================
# Created by: Alexander Kaier 
# Descript: Deleting FASTA header and appending sequences by ";1" as allergen flag
'''
with open(outFile, 'r') as fasta:
    for line in fasta:
        line = line.strip()
        if line.startswith(">"):
            line = line.replace(line[:], "")
        line = line + ";1"
        
    
        print(line)

import fileinput

for line in fileinput.input("../data/allergenonline.fasta", inplace=True):
    print "%d: %s" % (fileinput.filelineno(), line),
'''

