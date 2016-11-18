use python2.7

install tensorflow

create directories:
       train, out and imagenet_train
       
put the raw training data in the 'train' directory
create 'out' directory
run image_to_tfrecord.py to convert jpegs to tfrecords: the tfrecord shards will be in the 'out' directory

run train.py

