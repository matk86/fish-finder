#!/bin/bash

if [ "${PWD##*/}"  != "datasets" ]; then
    echo "Wrong directory, go to fish_finder/datasets"
else
    # Download inception weights
    wget http://download.tensorflow.org/models/inception_v4_2016_09_09.tar.gz
    tar xzvf inception_v4_2016_09_09.tar.gz inception_v4.ckpt
    rm inception_v4_2016_09_09.tar.gz

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
fi
