import os
import shutil
import numpy as np


labels = ["ALB", "BET", "DOL", "LAG", "NoF", "OTHER", "SHARK", "YFT"]

data_dir = os.path.expanduser("~/scratch/full/train/") # directory containing all the data
validation_dir = "validation"
training_dir = "train"

ntotal = 0
for l in labels:
    src_dir = os.path.join(data_dir, l)
    files = os.listdir(src_dir)
    nfiles = len(files)
    ntotal += nfiles
    print(nfiles, ntotal)
    nvalidation_samples = 1 # int(nfiles*0.1))
    ntrain_samples = 5 #nfiles - nvalidation_samples
    train_samples = np.random.choice(files, ntrain_samples)
    validation_samples = np.random.choice(files, nvalidation_samples)
    train_dir = os.path.join(training_dir, l)    
    val_dir = os.path.join(validation_dir, l)
    os.mkdir(train_dir)    
    os.mkdir(val_dir)
    for ts in train_samples:
        shutil.copy(os.path.join(src_dir, ts), train_dir)
    for vs in validation_samples:
        shutil.copy(os.path.join(src_dir, vs), val_dir)
        
