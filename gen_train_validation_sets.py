"""
Split the raw data into training and validation sets
"""
import os
import shutil
import numpy as np


labels = ["ALB", "BET", "DOL", "LAG", "NoF", "OTHER", "SHARK", "YFT"]

data_dir = os.path.expanduser("~/workspace/fisheries/datasets/train") # directory containing all the data
validation_dir = os.path.expanduser("~/workspace/validation")
training_dir = os.path.expanduser("~/workspace/train")
#nvalidation_samples = 1 
#ntrain_samples = 5


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
        dest_dir = val_dir if f in validation_samples else train_dir
        shutil.copy(os.path.join(src_dir, f), dest_dir)

        
