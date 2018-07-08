#!/usr/bin/env python

"""
Generate file_paths of specific type.
"""

import os
import os.path

ROOT_DIR = "/home/damon/work/datasets/ImageNet/trainset/ILSVRC/Data/DET/train"
OUTPUT_FILE = os.path.join(ROOT_DIR, "trainset.txt")


def generate_list(root_dir, fp):
    for parent, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            generate_list(os.path.join(root_dir, dirname), fp)

        file_lists = []
        for filename in filenames:
            (_, extname) = os.path.splitext(filename)
            if extname in [".JPEG", ".JPG", ".jpeg", ".jpg"]:
                file_lists.append(os.path.join(root_dir, filename + '\n'))
        fp.writelines(file_lists)


if __name__ == '__main__':
    with open(OUTPUT_FILE, 'w') as fp:
        generate_list(ROOT_DIR, fp)
