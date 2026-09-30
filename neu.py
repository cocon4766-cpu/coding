import numpy as np

def gradient(W,learning_rate):
   loss = (W - 5)**2
   print("The loss is :",loss) 
   gradient = 2*(W-5)
   print("The gradient is :",gradient)
   W2 = W - learning_rate * gradient
   print("The new weights is :",W2)
   new_loss = (W2 - 5)**2
   print("The new loss is :",new_loss)
   change_in_loss = new_loss - loss
   print("The change in loss is :",change_in_loss)
   gradient2 = 2*(W2 - 5)
   print("The gradient is :",gradient2)
   W3 = W2 - learning_rate * gradient2
   print("The new weights is :",W3)
   new_loss3 = (W3 - 5)**2
   print("The new loss is :",new_loss3)
W = 1.0
learning_rate = 0.1
gradient(W, learning_rate)