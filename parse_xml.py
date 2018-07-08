#!/usr/bin/env python

"""
Parse xml files and get specific fields.
"""

import xml.etree.ElementTree as ET

TEST_FILE = "/home/damon/work/datasets/ImageNet/trainset/ILSVRC/Annotations/DET/train/ILSVRC2013_train/n01443537/n01443537_12500.xml"

OBJECT_NODE = ['object']
LABEL_NODE = ['name']
BB_NODE = ['bndbox']
COORDINATE_NODE = ['xmin', 'xmax', 'ymin', 'ymax']


def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for o in OBJECT_NODE:
        o_node = root.find(o)
        for l in LABEL_NODE:
            l_node = o_node.find(l)
            print(l_node.tag + ": " + l_node.text)
        for b in BB_NODE:
            b_node = o_node.find(b)
            for c in COORDINATE_NODE:
                c_node = b_node.find(c)
                print(c_node.tag + ": " + c_node.text)


if __name__ == '__main__':
    parse_xml(TEST_FILE)

