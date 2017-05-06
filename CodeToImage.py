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
        for line in range(i, i + 36, 1):
            if line == length:
                break
            chunks.append(lines[line][0:72].rstrip('\n') + '\n')
    return chunks

# Open the file as a list of strings
open_file = open("orgn.f", 'r').readlines()

for chunk in chunk_file(open_file):
    for line in chunk:
        sys.stdout.write(line)
