from keras.datasets import mnist
(X,_),(_,_) = mnist.load_data()
print(X.shape)