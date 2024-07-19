#!/usr/bin/env python3

import os
import shutil
import sys
from math import ceil

def main():
    if len(sys.argv) != 2:
        print("Usage: python split_files.py /path/to/your/files/")
        sys.exit(1)

    directory = sys.argv[1]

    jpg_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    def match_files(jpg_files, txt_files):
        jpg_dict = {os.path.splitext(jpg)[0]: jpg for jpg in jpg_files}
        txt_dict = {os.path.splitext(txt)[0]: txt for txt in txt_files}
        pairs = []
        for key in jpg_dict.keys():
            if key in txt_dict:
                pairs.append((jpg_dict[key], txt_dict[key]))
        return pairs

    file_pairs = match_files(jpg_files, txt_files)

    total_pairs = len(file_pairs)
    half_size = ceil(total_pairs / 2)

    first_half = file_pairs[:half_size]
    second_half = file_pairs[half_size:]

    first_half_dir = os.path.join(directory, 'first_half')
    second_half_dir = os.path.join(directory, 'second_half')
    os.makedirs(first_half_dir, exist_ok=True)
    os.makedirs(second_half_dir, exist_ok=True)

    def move_files(file_pairs, dest_dir):
        for jpg, txt in file_pairs:
            shutil.move(os.path.join(directory, jpg), os.path.join(dest_dir, jpg))
            shutil.move(os.path.join(directory, txt), os.path.join(dest_dir, txt))

    move_files(first_half, first_half_dir)
    move_files(second_half, second_half_dir)

    print("Files have been split into two halves.")

if __name__ == "__main__":
    main()