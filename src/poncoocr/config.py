"""Module containing common variables and configurations for poncoocr modules."""

import os
import tensorflow as tf

# noinspection PyPackageRequirements
from src import data

_data_dir = os.path.dirname(data.__file__)

# shape of the thumbnail for the embedding
IMAGE_SHAPE = [32, 32]
THUMBNAIL_SHAPE = [32, 32]
EMBEDDING_SIZE = 1024

# set up simple object holding tensor name constants
EMBEDDING_TENSORS = type('', (), {})
EMBEDDING_TENSORS.BATCH_LABELS = 'batch_labels'
EMBEDDING_TENSORS.BATCH_FEATURES = 'batch_features'
EMBEDDING_TENSORS.EMBEDDING_INPUT = 'embedding_input'

LABEL_TENSOR_PROTO_FP = 'label_meta.proto'


# Define TensorFlow numeric flags

tf.app.flags.DEFINE_integer(
    name='k_candidates',
    default=5,
    help="Number of candidate classes to predict."
)


tf.app.flags.DEFINE_integer(
    name='batch_size',
    default=None,
    help="Batch size which will be used for training"
)

tf.app.flags.DEFINE_float(
    name='learning_rate',
    default=None,
    help="Learning rate parameter used for training."
)

tf.app.flags.DEFINE_integer(
    name='embedding_size',
    default=EMBEDDING_SIZE,
    help="Number of images passed to the embedding."
)

# Define TensorFlow string flags

tf.app.flags.DEFINE_string(
    name='test_dir',
    default=os.path.join(_data_dir, 'char-dataset/test_data'),
    help="Path to the directory storing test data."
)

tf.app.flags.DEFINE_string(
    name='train_dir',
    default=os.path.join(_data_dir, 'char-dataset/train_data'),
    help="Path to the directory storing train data."
)

tf.app.flags.DEFINE_string(
    name='model_arch',
    default=os.path.join(_data_dir, 'model/default-architecture.yaml'),
    help="Path to the directory storing model architecture."
)

tf.app.flags.DEFINE_string(
    name='sprite_dir',
    default=os.path.join(_data_dir, 'sprites/'),
    help="Path to the directory storing data sprites and their metadata."
)
