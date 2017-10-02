#!/usr/bin/python3

"""

File: convert2b64.py
Author: Richard Myatt
1 October 2017

*******************************************************************************
*                                                                             *
*    PLEASE NOTE THAT THIS CODE WITHIN NOTE RUN WITHIN THE CODE PLAYGROUND    *
*    This code is related to https://code.sololearn.com/WUDLPY7kf40v/#html    *
*                                                                             *
*******************************************************************************

This is a command line tool written for linux and takes an input file which is
then converted to base64 and written to the output file.  Both the input and
output files should be specified on the command line.  If the output file does
not exist it will be created.

Only minimal verification is performed on the command line arguments.

Usage: ./convert2b64.py <input_file> <output_file>
"""

import os, sys, base64

if len(sys.argv) == 3 and os.path.isfile(sys.argv[1]):

    fileToConvert = sys.argv[1]
    fileToWrite   = sys.argv[2]

    with open(fileToConvert, 'rb') as f2c:
        contents = f2c.read()

    encoded = base64.b64encode(contents)

    with open(fileToWrite, 'wb') as f2r:
        f2r.write(encoded)
else:
    print('*** Usage: ./convert2b64.py <input_file> <output_file> ***')
