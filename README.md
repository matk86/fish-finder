use python2.7

install tensorflow

Generate random training and validation samples:

	 python gen_train_validation_sets.py
	
Convert jpegs to tfrecords:

	python image_to_tfrecord.py

cd models/slim

./scripts/finetune_inception_v4_on_fishes.sh


scratch folder: old dev scripts
