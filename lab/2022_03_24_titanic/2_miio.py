# test

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(z):
    """Compute the sigmoid function."""
    return 1 / (1 + np.exp(-z))

def logreg_inference(x, w, b):  # z = w.T x + b
    """Inference step for the logistic regression model."""
    logit = (
        x @ w) + b  # no need to transpose becuse there is no transpose for vectors in phyton
    p = sigmoid(logit)  # 1 / (1 + np.exp(-z))
    return p


def cross_entropy(P, Y):
    """Binary cross-entropy."""
    P = np.clip(P, 0.0001, 0.9999)  # forces the value to stay within range
    return (-Y * np.log(P) - (1 - Y) * np.log(1 - P)).mean()




def load_file(filename):
    data = np.loadtxt(filename)
    X = data[:, :-1]  # take all rows and all columns except last one
    Y = data[:, -1]
    return X, Y


data = np.load("model.npz")
w = data["arr_0"] # dictionary and can access with this keyword
b = data["arr_1"]
X, Y = load_file("titanic-test.txt")
P = logreg_inference(X,w,b)

prediction = (P>0.5)
accuracy = (prediction == Y).mean()
print("Test accuracy is:", accuracy*100)









