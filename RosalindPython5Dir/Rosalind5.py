#!/usr/bin/env python3
import re
import subprocess
import numpy
import sys

subprocess.call("./TextReader")

with open(r"Output.txt", "r") as f:
    f_contents = f.read()
    with open(f_contents.rstrip(), "r") as g:
        text = g.read()
        text = text.rstrip()
        words = text.split(' ')
        np_words = numpy.array(words)
        np_unique = numpy.unique(np_words, return_counts=True)
        for y in numpy.nditer(np_unique):
            print(f'{y[0]} {y[1]}')