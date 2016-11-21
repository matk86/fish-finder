use python2.7

install tensorflow

Folders:

	train: raw training data, 

	validation: raw validation data

	data: processed data(both training and validation data in TFRecord format)
	
	imagenet_train: training checkpoint folder


Note:

	run gen_train_validation_sets.py to generate random training and validation samples
	
	run image_to_tfrecord.py to convert jpegs to tfrecords

	run train.py to train

	run evaluate_*.py to evaluate training or validation data
	
	The changes done to the original inception model are minor and
	almost no changes in the modules in the inception subpackage. 


TODO:

	update solver.py

	update/modify the image pre-processing.

	Change FLAGS settings in the modules.

	full test
	