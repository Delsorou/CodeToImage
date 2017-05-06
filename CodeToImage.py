#* -----------------------------------------------------------------------------
#
# FILE:              ----- FILE NAME -----
#
# DESCRIPTION:       ----- FILE DESCRIPTION -----
#
# DEVELOPED WITH:    ----- COMPILER AND SYSTEM -----
#
# NOTES:             ----- NOTES -----
#
# VERSION:           ----- VERSION -----
#
#---------------------------------------------------------------------------- *#

import os
import sys

#* -----------------------------------------------------------------------------
# FUNCTION:          ----- NAME -----()
# DESCRIPTION:       ----- DESCRIPTION -----
# RETURNS:           ----- TYPE ----- OR: nothing
# NOTES:             ----- NOTES -----
# --------------------------------------------------------------------------- /#
def chunk_file(lines):
    length = len(lines)

    chunks = []
    for i in range(0, length, 36):
        chunk = []
        for line in range(i, i + 36, 1):
            if line == length:
                break
            chunk.append(lines[line][0:72].rstrip('\n') + '\n')
        chunks.append(chunk)
    return chunks

# Open the file as a list of strings
open_file = open("orgn.f", 'r').readlines()

chunks = chunk_file(open_file)
new_chunks = enumerate(chunks)

for chunk in new_chunks:
    output = open(str(chunk[0]) + ".ch", 'w')
    for line in chunk[1]:
        output.write(line)
