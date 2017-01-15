#!/usr/bin/python2
"""
Split the raw data into training and validation sets
"""

import os
import shutil
import numpy as np
from PIL import Image

labels = ["ALB", "BET", "DOL", "LAG", "NoF", "OTHER", "SHARK", "YFT"]

data_dir = os.path.expanduser("./train") # directory containing all the data
validation_dir = os.path.expanduser("./data/validation")
training_dir = os.path.expanduser("./data/train")

ntotal = 0
for l in labels:
    src_dir = os.path.join(data_dir, l)
    files = os.listdir(src_dir)
    nfiles = len(files)
    ntotal += nfiles
    print(nfiles, ntotal)
    nvalidation_samples = int(nfiles*0.1) # 10% of the data
    validation_samples = np.random.choice(files, nvalidation_samples)
    train_dir = os.path.join(training_dir, l)    
    val_dir = os.path.join(validation_dir, l)
    os.mkdir(train_dir)    
    os.mkdir(val_dir)
    for f in files:
        src_file = os.path.join(src_dir, f)
        try:
            im = Image.open(src_file)
            im.verify()
        except:
            print("Issue with : {}".format(src_file))
            continue
        dest_dir = val_dir if f in validation_samples else train_dir
        shutil.copy(src_file, dest_dir)

        
