import numpy as np
import matplotlib.pyplot as plt

# exam.txt
# 1 feature h of study 
# 2 feature h in class
# 0 or 1 if passed or not


def sigmoid(z):
    """Compute the sigmoid function."""
    return 1 / (1 + np.exp(-z))


def logreg_inference(x, w, b): # z = w.T x + b 
    """Inference step for the logistic regression model."""
    logit  = (x @ w) + b # no need to transpose becuse there is no transpose for vectors in phyton
    p = sigmoid(logit)  # 1 / (1 + np.exp(-z))
    return p


def cross_entropy(P, Y):
    """Binary cross-entropy."""
    return (-Y * np.log(P) - (1 - Y) * np.log(1 - P)).mean()


def logreg_train(X, Y):
    """
    Training procedure for the logistic regression model. 
    Use gradient decend   
    w' = w - eta * gradient(L)   w.r.t. w
    b' = b - eta * gradient(L)   w.r.t. b
    """
    m, n = X.shape
    w = np.zeros(n)
    b = 0   # convex function doesn't matter where we start
    lr = 0.01   # learning rate
    for step in range(100000):
        P = logreg_inference(X, w, b)
        if step % 1000 == 0: # to print every thousand cycles
            loss = cross_entropy(P, Y)
            print(step, loss)
        grad_w = (X.T @ (P - Y)) / m  # gradient w.r.t. w
        grad_b = (P - Y).mean()       # gradient w.r.t. b
        # Gradient descent updates.
        
        w -= lr * grad_w  # e qui li aggiorno
        b -= lr * grad_b
    return w, b


# Load the data, train the mnodel and measure the accuracy.
data = np.loadtxt("exam.txt")  # returns the matrix
X = data[:, :-1]  # :2
Y = data[:, -1]
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.show()
w, b = logreg_train(X, Y)
P = logreg_inference(X, w, b)
Yhat = (P >= 0.5) # prediction
accuracy = (Y == Yhat).mean()
print("Accuracy:", accuracy * 100)
