from dataset import Dataset

# implementation of the abstract Dataset class in the dataset module
class FishData(Dataset):

  def __init__(self, subset):
    super(FishData, self).__init__('Fish', subset)
    
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


