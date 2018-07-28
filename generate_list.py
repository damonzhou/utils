#!/usr/bin/env python

"""
Generate file_paths of specific type.
"""

import os
import os.path
import stat
import argparse
from enum import Enum
from os.path import exists

ROOT_DIR = "/home/damon/work/datasets/ImageNet/trainset/ILSVRC/Data/DET/train"
OUTPUT_FILE = os.path.join(ROOT_DIR, "trainset.txt")


class FileTypes(Enum):
    IMAGE = 0
    LABEL = 1


# Is a path a directory?
# This follows symbolic links, so both islink() and isdir()
# can be true for the same path on systems that support symlinks
def isdir(s):
    """Return true if the pathname refers to an existing directory."""
    try:
        st = os.stat(s)
    except OSError:
        return False
    return stat.S_ISDIR(st.st_mode)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", required=True, help="Image or Label", type=str)
    parser.add_argument("-i", "--input_dir", required=True, help="Directory path", type=str)
    parser.add_argument("-o", "--output_file", required=True, help="Output file name", type=str)

    args = parser.parse_args()
    assert (isdir(args.input_dir)), \
        "Please check if directory exists."
    if exists(os.path.join(args.input_dir, args.output_file)):
        print("WARN: Overriding existed output file.")
    return args


def generate_list(root_dir, fp):
    if file_type == FileTypes.IMAGE:
        extnames = [".JPEG", ".JPG", ".jpeg", ".jpg"]
    elif file_type == FileTypes.LABEL:
        extnames = [".json", ".xml"]

    for parent, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            generate_list(os.path.join(root_dir, dirname), fp)

        file_lists = []
        for filename in filenames:
            (_, extname) = os.path.splitext(filename)
            if extname in extnames:
                file_lists.append(os.path.join(root_dir, filename + '\n'))
        fp.writelines(file_lists)


if __name__ == '__main__':
    args = parse_args()
    if args.type == 'Image':
        file_type = FileTypes.IMAGE
    elif args.type == 'Label':
        file_type = FileTypes.LABEL
    else:
        print("Type string not supported!")
        exit(-1)

    of = os.path.join(args.input_dir, args.output_file)

    with open(of, 'w') as fp:
        generate_list(args.input_dir, fp)
