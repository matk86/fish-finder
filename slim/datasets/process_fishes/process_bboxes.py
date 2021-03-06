"""
Use the bbox json files downloaded from kaggle and generate normalized bbox for each image in
the training set and write it to json and csv files.
"""

import os
from glob import glob
import json
import csv
from PIL import Image

# path to the raw training data directory
train_data_dir=os.path.abspath(os.path.expanduser("~/workspace/fisheries/datasets/train"))
all_train_images=glob(train_data_dir+"/*/*.jpg")

# map iamge filename --> full path
img_name_path_dict = {}
for ip in all_train_images:
    img_name_path_dict[os.path.basename(ip)] = ip

# all bbox data files(from kaggle)
json_files = glob("*_labels.json")

alld_dict = {}

for jf in json_files:
    d = json.load(open(jf,"r"))
    for dct in d:
        area = 0
        if "annotations" in dct:
            for anot in dct["annotations"]:
                image_path = img_name_path_dict[os.path.basename(dct["filename"])]
                img = Image.open(image_path)
                W, H = img.size
                x0 ,y0, w0, h0 = anot["x"], anot["y"], anot["width"], anot["height"]
                x, y, w, h = x0 ,y0, w0, h0
                # if the bbox area is negative, skip the current iteration
                if w0*h0 < 0:
                    print("negative area: {}".format(dct["filename"]))
                    continue
                # pick the bbox with the max area
                if w0*h0 >= area:
                    x, y, w, h = x0 ,y0, w0, h0
                    area = w*h                    
                xmin, ymin, xmax, ymax = x ,y, x+w, y+h
                # normalize x and y
                xmin_n, ymin_n, xmax_n, ymax_n = xmin/W ,ymin/H, xmax/W, ymax/H
                    
            #alld_dict[dct["filename"].split("/")[-1]] = [x, y, w, h]

            min_x = min(xmin_n, xmax_n)
            max_x = max(xmin_n, xmax_n)
            xmin_scaled = min(max(min_x, 0.0), 1.0)
            xmax_scaled = min(max(max_x, 0.0), 1.0)
            
            min_y = min(ymin_n, ymax_n)
            max_y = max(ymin_n, ymax_n)
            ymin_scaled = min(max(min_y, 0.0), 1.0)
            ymax_scaled = min(max(max_y, 0.0), 1.0)
            
            if (abs(xmin_scaled - 1.0)<=1e-2 and abs(ymin_scaled - 1.0)<=1e-2) or (abs(xmax_scaled)<=1e-2 and abs(ymax_scaled)<=1e-2) :
                xmin_scaled, ymin_scaled, xmax_scaled, ymax_scaled = 0.0, 0.0, 1.0, 1.0
            #alld_dict[dct["filename"].split("/")[-1]] = [xmin, ymin, xmax, ymax]
            alld_dict[dct["filename"].split("/")[-1]] = [xmin_scaled, ymin_scaled, xmax_scaled, ymax_scaled]
        else:
            print("no annotations: {}".format(dct))
    #alld.extend(d)


fname = "bboxes_min_max_scaled_coords.json"

# dump to json
json.dump(alld_dict, open(fname, "w"))
print(len(alld_dict))

# dump to csv
with open(fname.replace(".json", ".csv"), 'w') as f:
    writer = csv.writer(f)
    for k, v in alld_dict.items():
        writer.writerow([k]+v)

