*** Data preparation

This directory contains code to prepare data for the bbox and fish identification NNs.

1. Put bbox-related json files from this [forum post]
(https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring/forums/t/25902/complete-bounding-box-annotation)
into ./orig_bbox_labels/. Note: not all json files are in OP?

1. Unzip Kaggle-provided train.zip to create ./train with subdirectories ALB, BET, etc.

1. Run prepare_data.sh. Sharded train-* and validation-* files will be created.

TODO: consider incorporating mouth/tail data.
