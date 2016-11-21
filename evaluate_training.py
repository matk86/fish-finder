import tensorflow as tf
from fish_data import FishData
from evaluate import evaluate


def main(_):
    dataset = FishData("train")
    assert dataset.data_files()
    if tf.gfile.Exists(FLAGS.eval_dir):
      tf.gfile.DeleteRecursively(FLAGS.eval_dir)
    tf.gfile.MakeDirs(FLAGS.eval_dir)
    evaluate(dataset)

if __name__ == '__main__':
  tf.app.run()
      
