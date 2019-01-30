# Implementation of deep learning framework -- Unet, using Keras

The architecture was inspired by [U-Net: Convolutional Networks for Biomedical Image Segmentation](http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/).

---

## Overview

### Data

You can find it in folder ``data/``
Download here (https://drive.google.com/open?id=1HpEk8HMoX2i0sjKKMw9Fbo3ipe_W9Yxz), then uncompress it.

### Model

![img/u-net-architecture.png](img/u-net-architecture.png)

This deep neural network is implemented with Keras functional API, which makes it extremely easy to experiment with different interesting architectures.

Output from the network is a 512 x 512 x 3 which represents inpainting image that should be learned.

## How to use

### Dependencies

This tutorial depends on the following libraries:

* Tensorflow
* Keras >= 1.0

Also, this code should be compatible with Python versions 2.7-3.5.

### Training

    python3 main.py

### Predict

After get model from training. Add path of `model` and `save path` in predict.py

    python3 predict.py
    
### Others

File | Descriptions
-----|------------
preprocess.py | blend fence to original data and split train:test set
model.py | autoencoder model in keras
data.py | preprocess image and make (samples, labels) pipeline, data augmentation for keras model

