See https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring.

Use python2.7 and install tensorflow.

## ./datasets
Prepare data as described in ./datasets.

## ./slim
Branched tf-slim code from the (non-core repo)[https://github.com/tensorflow/models/tree/master/slim]
modified for training and evaluating both the bboxes and classification NNs. 

### Training:

From the root of the git repo:

~~~
$ cd slim/datasets/process_fishes/
~~~

Generate bbox csv file (bboxes_min_max_scaled_coords.csv):

~~~
$ python process_bboxes.py
~~~

Generate data (i.e training and validation sets in tfrecord format) with bboxes:

~~~
$ ./preprocess_fishes.sh ../../../datasets/data/train/ ../../../datasets/data/processed labels.txt bboxes_min_max_scaled_coords.csv 10
~~~
        
Train net 1(regression) and net 2(classification) independently(using the same set of data). From the root of the git repo:

~~~
cd slim
# Run regression:
./scripts/finetune_inception_v4_on_fishes.sh ../datasets ./tmp/regression/logs ../datasets/data/processed reg 3777 355 5000 32 0.0001
# Run classification:
./scripts/finetune_inception_v4_on_fishes.sh ../datasets ./tmp/classification/logs ../datasets/data/processed class 3777 355 5000 32 0.0001
~~~    

### Testing:

The `tester.sh` script does the following:

- Convert  the raw testing data to tfrecord data without the bbox
- Run net 1 on the above data and write the bbox predictions to csv file
- Generate data using the raw data and the bbox csv file
- Run net 2 and write the logits to csv

From the root of the git repo:

~~~
cd slim
./scripts/tester.sh ../datasets/test_stg1 ./tmp/regression ./tmp/classification 1000 20
~~~

# Server Info
### Access
`ubuntu@ec2-35-161-84-178.us-west-2.compute.amazonaws.com`

### Directory 
TODO: Put general directory layout here. 

# Tensorboard
### Start Tensorboard on Server
`tensorboard --logdir=~/workspace/fish_finder/slim/tmp`
### SSH Tunnel to view Tensorboard
`ssh -L 16006:127.0.0.1:6006 ubuntu@35.164.223.134 -N -v`

go to: http://127.0.0.1:16006/
