# Implementation of deep learning framework -- Gan, using Keras
## Overview
### Model
Document : https://skymind.ai/wiki/generative-adversarial-network-gan
            
Model :

![gan/g1.jpg](gan/g1.jpg)
![gan/GANs.png](gan/GANs.png)


## How to use

### Dependencies

    This tutorial depends on the following libraries:

    * Keras >= 1.0

    Also, this code should be compatible with Python versions 2.7-3.5.
    
### Dataset 

    Dataset is mnist in keras library

### Training

    Have 2 temporary files are sigmoid.py and tanh.py <=> 2 activation function of last layer in generator
    commandline : python3 sigmoid.py or python3 tanh.py
    

### Result

    After model inpaint image, result images will save at images folder

### Note
    Gan model is unsupervised learning 

