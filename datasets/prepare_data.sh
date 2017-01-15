#!/bin/bash

# Create labels.json
cd orig_bbox_labels
echo Num records:
./process_box_data.py 
cd ..

# Create train/validation datasets
mkdir -p data/{validation,train} 2>/dev/null
./gen_train_validation_sets.py

#
./image_to_tfrecord.py \
    --train_directory ./data/train \
    --validation_directory ./data/validation \
    --output_directory ./
