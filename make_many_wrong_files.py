#!/usr/bin/env python

import random
def get_name():
    l = random.randint(5, 10)
    s = random.choices("atgc", k=l)
    s = "".join(s)
    return s


import os
try:
    os.mkdir("wrong")
except FileExistsError:
    pass
for i in range(1000):
    name = get_name()
    with open(f"wrong/{name}.txt.gz", "w"):
        pass
