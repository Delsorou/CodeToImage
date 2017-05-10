#* -----------------------------------------------------------------------------
#
# FILE:              CodeToImage.py
#
# DESCRIPTION:       Program to convert Fortran source code into images
#                    suitable for use with Spring 2017 ART100 Final
#
# DEVELOPED WITH:    Python 2.7.13
#
# DEPENDENCIES:      python-pil 4.0.0-4, python-pygments 2.2.0
#
# NOTES:             None
#
# VERSION:           0.0
#
#---------------------------------------------------------------------------- *#

from ron import RonStyle 
from pygments import highlight
from pygments.lexers import FortranLexer
from pygments.formatters import ImageFormatter

#* -----------------------------------------------------------------------------
# FUNCTION:          chunk_strings()
# DESCRIPTION:       Creates square chunks of text from a list of strings
# RETURNS:           enumerated list of lists of strings
# NOTES:             None
# --------------------------------------------------------------------------- /#
def chunk_text(lines):
    length = len(lines)
    chunks = []
    for i in range(0, length, 36):
        chunk = "" 
        for line in range(i, i + 36, 1):
            if line == length:
                break
            chunk += lines[line][0:72].rstrip('\n') + '\n'
        chunks.append(chunk)
    enum_chunks = enumerate(chunks)
    return enum_chunks

# Open the file as a list of strings
open_file = open("orgn.f", 'r').readlines()

for chunk in chunk_text(open_file):
    output_file = open(str(chunk[0]) + ".png", 'w')
    output = highlight(chunk[1], FortranLexer(),
            ImageFormatter(font_size=14,
            font_name="FreeMono", line_numbers=False,
            style=RonStyle, image_pad=0, line_pad=1))
    output_file.write(output)
