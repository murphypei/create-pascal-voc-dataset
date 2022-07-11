#! -*- coding:utf-8 -*-

import re
import os
import sys


def parse_annotation(inria_dir, phase, verbose=True):

    anno_dir = os.path.join(inria_dir, phase, 'annotations')

    image_path_tmpl = re.compile(r'Image filename : "([\w\d/_.]+)"')
    object_box_tmpl = re.compile(
        r'Bounding box for object [\d]+ \"([\w]+)\"[-,\(\)\w\s]+ : \((\d+), (\d+)\) - \((\d+), (\d+)\)$')

    fout = open(os.path.join(inria_dir, phase, '{}_annotation.txt'.format(phase)), 'w')

    for anno_file in os.listdir(anno_dir):
        with open(os.path.join(anno_dir, anno_file), 'r') as f:
            result = []
            for line in f:
                line = line.strip()
                if line.startswith("Image filename"):
                    img_path = image_path_tmpl.match(line).group(1)
                    if verbose:
                        print("process image: {}".format(img_path))
                    img_full_path = os.path.join(inria_dir, img_path)
                    result.append(img_full_path)

                # search object box
                if line.startswith("Bounding box for object"):
                    if verbose:
                        print("find a object...")
                    sg = object_box_tmpl.match(line)
                    box = [sg.group(1), sg.group(2), sg.group(3), sg.group(4), sg.group(5)]
                    box_str = ' '.join(box)
                    result.append(box_str)
            fout.write(' '.join(result) + '\n')

    fout.close()


if __name__ == "__main__":

    inria_dir = sys.argv[1]

    parse_annotation(inria_dir, 'Train', True)
    parse_annotation(inria_dir, 'Test', True)
