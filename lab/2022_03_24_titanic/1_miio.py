#
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


def logreg_train(X, Y, lr, steps):
    m, n = X.shape
    w = np.zeros(n)
    b = 0   # convex function doesn't matter where we start
    accuracies = []
    losses = []
    for step in range(steps):
        P = logreg_inference(X, w, b)
        if step % 1000 == 0:  # to print every thousand cycles
            loss = cross_entropy(P, Y)
            prediction = (P > 0.5)
            accuracy = (Y == prediction).mean()
            print(step, loss, accuracy * 100)
            losses.append(loss)
            accuracies.append(accuracy)
        grad_w = (X.T @ (P - Y)) / m  # gradient w.r.t. w
        grad_b = (P - Y).mean()       # gradient w.r.t. b
        # Gradient descent updates.

        w -= lr * grad_w  # e qui li aggiorno
        b -= lr * grad_b
    return w, b, losses, accuracies


def load_file(filename):
    data = np.loadtxt(filename)
    X = data[:, :-1]  # take all rows and all columns except last one
    Y = data[:, -1]
    return X, Y


X, Y = load_file("titanic-train.txt")
print(X.shape)
print(Y.shape)
lr = 0.003
step = 100000
me = np.array([1, 0, 50, 0, 3, 100])    # classe, 0 M  1 F, age, parenti
w, b, losses, accuracies = logreg_train(
    X, Y, lr, step)  # x, y, learning rate, step
P = logreg_inference(me, w, b)  # estrae la prob di sopravvivere
print("w=", w)
print("b=", b)

plt.plot(losses)
plt.ylabel("losses")
plt.figure()

plt.plot(accuracies)
plt.ylabel("accuracies")
plt.show()

print("prob of survival = ", P)

# se un weigth è positivo vuol dire che quella caratteristica aumenta la prob di sopravvivenza

# femmine di prima classe vivono, maschi ultima muiono

# add random noise to see how many are them
Xrnd = X + np.random.randn(X.shape[0], X.shape[1]) / 20
plt.scatter(Xrnd[:,0], Xrnd[:,-1], c = Y)
plt.xlabel("Ticket class")
plt.ylabel("ticket fare")
# plt.ylabel("sex")
plt.show()

np.savez("model.npz", w, b)# salva le variabili del training