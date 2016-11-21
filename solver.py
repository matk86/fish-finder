import tensorflow as tf

from dataset import Dataset
from train import train
from evaluate import evaluate

# implementation of the abstract Dataset class in the dataset module
class Dset(Dataset):

  def num_classes(self):
    """Returns the number of classes in the data set."""
    return 8

  def num_examples_per_epoch(self):
    """Returns the number of examples in the data subset."""
    # total 3777
    if self.subset == 'train':
       return 1 #3000
    if self.subset == 'validation':
       return 1 #777


def main(_):
    training_set = Dset("train", "train")
    validation_set = Dset("validation", "validation")    
    nepochs = 1 #20
    for i in range(nepochs):      
      train(training_set)
      # evaluate training accuracy
      #evaluate(training_set)
      # compute validation accuracy
      #evaluate(validation_set)      


if __name__ == '__main__':
  tf.app.run()


# all hyper-parameters aka flags
#print(tf.app.flags.FLAGS.__dict__['__flags'])
#{'subset': 'train',
# 'pretrained_model_checkpoint_path': '',
# 'learning_rate_decay_factor': 0.16,
# 'eval_interval_secs': 300,
# 'checkpoint_dir': 'imagenet_train',
# 'data_dir': 'data',
# 'num_examples': 50000,
# 'run_mode': 'validation',
# 'input_queue_memory_factor': 4,
# 'num_readers': 2,
# 'num_epochs_per_decay': 30.0,
# 'batch_size': 32,
# 'run_once': False,
# 'image_size': 299,
# 'num_preprocess_threads': 4,
# 'log_device_placement': False,
# 'eval_dir': 'imagenet_eval',
# 'num_gpus': 1,
# 'train_dir': 'imagenet_train',
# 'initial_learning_rate': 0.1,
# 'fine_tune': False,
# 'max_steps': 1}
