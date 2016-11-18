use python2.7

install tensorflow

create directories:

       train, out and imagenet_train
       
put the raw training data in the 'train' directory

create 'out' directory

run image_to_tfrecord.py to convert jpegs to tfrecords: the tfrecord shards will be in the 'out' directory

run train.py


Note: The changes done to the original inception model are minor and almost no changes
in the modules in the inception subpackage. 


TODO: update/modify the image pre-processing. Change FLAGS settings in the modules.
