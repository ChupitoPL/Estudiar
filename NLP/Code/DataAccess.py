import pandas as pd
import os


def read_single_file(dir, subdir, filename):
    with open(r'.\Data\{}\{}\{}'.format(dir, subdir, filename), 'r') as f:
        data = f.read()
    return data

print(read_single_file("train", "neg", "1_1.txt"))
