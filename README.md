use python2.7

install tensorflow

Generate random training and validation samples:

	 python gen_train_validation_sets.py
	
Convert jpegs to tfrecords:

	python image_to_tfrecord.py

cd models/slim

./scripts/finetune_inception_v4_on_fishes.sh


scratch folder: old dev scripts

# Server Info
### Access
`ubuntu@ec2-35-161-84-178.us-west-2.compute.amazonaws.com`

### Directory 
TODO: Put general directory layout here. 

# Tensorboard
### Start Tensorboard on Server
`tensorboard --logdir=/tmp/fishes/inception_v4/`
### SSH Tunnel to view Tensorboard
`ssh -L 16006:127.0.0.1:6006 ubuntu@ec2-35-161-84-178.us-west-2.compute.amazonaws.com -N -v`

go to: http://127.0.0.1:16006/
