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
       return 3000
    if self.subset == 'validation':
       return 777


def main(_):
    training_set = Dset("train", "train")
    validation_set = Dset("validation", "validation")    
    nepochs = 1 #20
    for in in rnage(nepochs):
      train(training_set)
      # evaluate training accuracy
      #evaluate(training_set)
      # compute validation accuracy
      #evaluate(validation_set)      


if __name__ == '__main__':
  tf.app.run()
