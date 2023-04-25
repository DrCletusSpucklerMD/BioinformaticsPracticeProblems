#!/usr/bin/python
import sys
import os
import re
import subprocess


subprocess.call("./TextReader")

with open(r"../RosalindPython5Dir/Output.txt", "r") as f:
    f_contents = f.read()
    with open(f_contents.strip(), "r") as g:
        DNAstring = g.read()

        A_count = DNAstring.count("A")
        C_count = DNAstring.count("C")
        G_count = DNAstring.count("G")
        T_count = DNAstring.count("T")


        print A_count, C_count, G_count, T_count
        #sys.stdout.write(str(A_count))





