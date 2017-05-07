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

from PIL import Image, ImageDraw, ImageFont

#* -----------------------------------------------------------------------------
# FUNCTION:          chunk_strings()
# DESCRIPTION:       Creates square chunks of text from a list of strings
# RETURNS:           enumerated list of lists of strings
# NOTES:             None
# --------------------------------------------------------------------------- /#
def chunk_strings(lines):
    length = len(lines)
    chunks = []
    for i in range(0, length, 36):
        chunk = []
        for line in range(i, i + 36, 1):
            if line == length:
                break
            chunk.append(lines[line][0:72].rstrip('\n') + '\n')
        chunks.append(chunk)
    enum_chunks = enumerate(chunks)
    return enum_chunks

# Open the file as a list of strings
open_file = open("orgn.f", 'r').readlines()

chunks = chunk_strings(open_file)

fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 12)
fontcolor = (0, 0, 0, 225)

for chunk in chunks:
    background = (0, 0, 0, 0)
    test_img = Image.new("RGBA", (1,1))
    test_draw = ImageDraw.Draw(test_img)
    
    # Concatenate the chunk for image processing
    string_chunk = ''
    for string in chunk[1]:
        string_chunk += string

    textsize = test_draw.textsize(string_chunk, fnt)

    file_img = Image.new("RGBA", textsize, background)
    file_draw = ImageDraw.Draw(file_img)

    file_draw.text((0, 0), string_chunk, fontcolor, fnt)
    file_img.save(str(chunk[0]) + ".png", "PNG")
