#!/usr/bin/env python3

class config_test(object):
    mode = 'alpha'
    n_layers = 5
    num_epochs = 512
    batch_size = 256
    ema_decay = 0.999
    learning_rate = 8e-4
    n_classes = 10
    conv_keep_prob = 1.0
    dense_keep_prob = 1.0
    im_x = 32
    im_y = 32
    g0 = 1e-2
    g1 = 1e-3
    L = 10
    lr_decay_rate = 2e-5

class config_train(object):
    mode = 'beta'
    n_layers = 5
    num_epochs = 512
    batch_size = 256
    ema_decay = 0.999
    learning_rate = 1e-3
    n_classes = 10
    conv_keep_prob = 0.7
    dense_keep_prob = 0.7
    im_x = 32
    im_y = 32
    g0 = 1e-2
    g1 = 1e-3
    L = 20
    lr_decay_rate = 5e-3
    momentum = 0.9
    weight_decay = 5e-4
    steps_per_epoch = 50000//batch_size

class directories(object):
    train = 'dataset/cifar10/cifar10_train.tfrecord' #'/var/local/tmp/jtan/cifar10/cifar10_train.tfrecord'
    test = 'dataset/cifar10/cifar10_test.tfrecord' #'/var/local/tmp/jtan/cifar10/cifar10_test.tfrecord'
    tensorboard = 'tensorboard'
    checkpoints = 'checkpoints'
    checkpoints_best = 'checkpoints/best'
