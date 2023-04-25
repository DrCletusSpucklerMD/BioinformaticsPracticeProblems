#!/usr/bin/env python3

import subprocess
import numpy as np
import math

subprocess.call("./textReader2")

with open(r"Output.txt", "r", encoding="utf-8") as f:
    f_contents = f.read()
    file_name = f_contents.split()
    with open(file_name[4], "r", encoding="utf-8") as g:
        integer = g.read()
        integer = int(integer)
        components_list = np.array(range(1, integer+1))
        perm_array = np.array(components_list)

        num_perm = math.factorial(integer)
        print(num_perm)
        i = 0

        while i < num_perm:
            temp = np.random.permutation(perm_array)
            for x in perm_array:
                if perm_array.any() == temp:
                    break
                else:
                    i = i + 1
                    print("yes!")