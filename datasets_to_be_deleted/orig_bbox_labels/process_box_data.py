#!/usr/bin/python2

from glob import glob
import json

json_files = glob("*_labels.json")

alld_dict = {}

for jf in json_files:
    d = json.load(open(jf,"r"))
    for dct in d:
        area = 0
        if "annotations" in dct:
            for anot in dct["annotations"]:
                x0 ,y0, w0, h0 = anot["x"], anot["y"], anot["width"], anot["height"]
                if w0*h0 < 0:
                    print("neagtive area: {}".format(dct["filename"]))
                    continue
                if w0*h0 >= area:
                    x, y, w, h = x0 ,y0, w0, h0
                    area = w*h
            alld_dict[dct["filename"].split("/")[-1]] = [x, y, w, h]
        else:
            print("no annotations: {}".format(dct))
    #alld.extend(d)

json.dump(alld_dict, open("../bboxes.json", "w"))
print(len(alld_dict))
