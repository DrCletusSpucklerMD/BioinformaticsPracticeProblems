#!/usr/bin/env python3

import subprocess
import numpy as np
import sys

subprocess.call("./textReader")

with open(r"Output.txt", "r", encoding="utf-8") as f:
    f_contents = f.read()
    with open(f_contents.rstrip(), "r", encoding="utf-8") as g:
        text = g.read()
        text = text.split()

        a = list(text[0])
        b = list(text[1])

        j = 0
        counter = 0

        for i in a:
            if i != b[j]:
                counter = counter + 1
            j = j + 1

        print(counter)
